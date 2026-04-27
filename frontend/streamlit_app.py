import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# --- Configuration ---
# Get the URL from the .env file (defaults to localhost if the .env variable is missing)
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api")
PAGE_TITLE = "QueryCortex AI"
PAGE_ICON = "🧠"

# --- Page Setup ---
st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON, 
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0;
    }
    .footer { text-align: center; padding-top: 20px; border-top: 1px solid #e6e6e6; }
    .status-badge { padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .status-ok { background-color: #d1fae5; color: #065f46; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "token" not in st.session_state: st.session_state.token = None
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "active_docs" not in st.session_state: st.session_state.active_docs = []
if "db_sessions" not in st.session_state: st.session_state.db_sessions = []

# --- Helper Functions ---
def get_headers():
    return {"Authorization": f"Bearer {st.session_state.token}"} if st.session_state.token else {}

def api_request(method, endpoint, data=None, json_data=None, files=None):
    url = f"{API_BASE_URL}{endpoint}"
    headers = get_headers()
    try:
        if method == "GET": response = requests.get(url, headers=headers)
        elif method == "POST": response = requests.post(url, headers=headers, data=data, json=json_data, files=files)
        
        if response.status_code == 401:
            st.session_state.token = None
            st.rerun()
        return response
    except Exception:
        st.error("🔌 Backend unreachable.")
        return None

def update_active_session():
    """Fetches list of active documents."""
    resp = api_request("GET", "/documents/active_session")
    if resp and resp.status_code == 200:
        st.session_state.active_docs = resp.json().get("data", {}).get("files", [])

def update_db_sessions():
    """Fetches saved database connections."""
    resp = api_request("GET", "/db/list_sessions")
    if resp and resp.status_code == 200:
        st.session_state.db_sessions = resp.json().get("data", {}).get("sessions", [])
    
def clear_active_db_sessions():
    """Clears all active database connections."""
    resp = api_request("POST", "/db/clear_active_sessions", json_data={"delete_all": True})
    if resp and resp.status_code == 200:
        update_db_sessions()

# --- UI Components ---

def login_view():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<h1 style='text-align: center;'>{PAGE_ICON} QueryCortex AI</h1>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
        with tab1:
            with st.form("login"):
                u = st.text_input("Username")
                p = st.text_input("Password", type="password")
                if st.form_submit_button("Login", use_container_width=True):
                    with st.spinner("Authenticating..."): # Rotating wheel
                        resp = api_request("POST", "/login", data={"username": u, "password": p})
                        if resp and resp.status_code == 200:
                            st.session_state.token = resp.json()["access_token"]
                            st.rerun()
        with tab2:
            with st.form("signup"):
                e, n, un, pw = st.text_input("Email"), st.text_input("Full Name"), st.text_input("Username"), st.text_input("Password", type="password")
                if st.form_submit_button("Create Account", use_container_width=True):
                    with st.spinner("Creating account..."):
                        resp = api_request("POST", "/signup", json_data={"email": e, "name": n, "username": un, "password": pw})
                        if resp and resp.status_code == 200: st.success("Created! Please login.")

def sidebar_view():
    st.sidebar.title(f"{PAGE_ICON} QueryCortex AI")
    st.sidebar.markdown(f"**User Status:** <span class='status-badge status-ok'>Online</span>", unsafe_allow_html=True)
    if st.sidebar.button("Logout", use_container_width=True):
        resp = api_request("POST", "/logout")
        if resp and resp.status_code == 200:
            st.session_state.token = None
            st.rerun()
    
    st.sidebar.divider()

    # 1. Database Management
    with st.sidebar.expander("🛢️ Database Hub", expanded=False):
        # New Connection Form
        with st.form("db_form"):
            db_type = st.selectbox("Type", ["postgresql","databricks", "mysql"])
            h, p = st.text_input("Host", "localhost"), st.number_input("Port", 5432)
            db_name, u, pwd = st.text_input("DB Name"), st.text_input("User"), st.text_input("Password", type="password")
            if st.form_submit_button("Connect & Save"):
                payload = {"db_type": db_type, "host": h, "port": p, "database": db_name, "username": u, "password": pwd}
                with st.spinner("Connecting to DB..."): # Rotating wheel
                    resp = api_request("POST", "/db/add_or_connect", json_data=payload)
                    if resp and resp.status_code == 200: 
                        st.success("Connected!")
                        update_db_sessions()
        
        # Saved Sessions List
        st.markdown("---")
        st.caption("Saved Databases")
        if st.button("🔄 Refresh Sessions"):
            update_db_sessions()
        if not st.session_state.db_sessions:
            st.warning("⚠️ No database sessions found. Please use the form above to connect your first database.")
        else:
            for s in st.session_state.db_sessions:
                col_a, col_b = st.columns([4, 1])
                # col_a.text(f"{'🟢' if s['connection_status'] else '⚪'} {s['database']}")
                status_text = "Active/Connected" if s['connection_status'] else "Inactive/Disconnected"
                status_emoji = "🟢" if s['connection_status'] else "⚪"

                # Using markdown with 'help' for the hover effect
                col_a.markdown(
                    f"{status_emoji} {s['database']}", 
                    help=f"Status: {status_text})"
                )

                if col_b.button("🔌", key=f"rec_{s['id']}",help=f"Reconnect to {s['database']} ({s['db_type']})"):
                    with st.spinner("Reconnecting..."):
                        api_request("POST", "/db/reconnect", json_data={"db_id": s['id']})
                        update_db_sessions()
                        st.rerun()
                
    # 2. Document Management
    with st.sidebar.expander("📜 Document Hub", expanded=True):
        uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])
        if uploaded_file and st.button("Process & Upload", use_container_width=True):
            with st.spinner("Analyzing PDF..."): # Rotating wheel
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                resp = api_request("POST", "/documents/upload", files=files)
                if resp and resp.status_code == 200: 
                    st.success("Uploaded!")
                    update_active_session()
        st.markdown("---")
        st.caption("Documents in Current Session")
        if st.session_state.active_docs:
            for doc in st.session_state.active_docs:
                c1, c2 = st.columns([4, 1])
                c1.caption(f"📜 {doc}")
                if c2.button("🗑️", key=f"del_{doc}",help=f"Remove {doc} from active session"):
                    with st.spinner("Removing..."):
                        api_request("POST", "/documents/clear_session", json_data={"filename": doc, "delete_all": False})
                        update_active_session()
                        st.rerun()
            
            if st.button("Clear All Documents", use_container_width=True):
                with st.spinner("Clearing all..."):
                    api_request("POST", "/documents/clear_session", json_data={"delete_all": True})
                    update_active_session()
                    st.rerun()
        else:
            st.warning("⚠️ No Documents in Active Session.You can upload new documents.")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("<div style='text-align: center; font-size: 0.8rem;'>Developed by Shib Kumar Saraf<br>© 2026 QueryCortex</div>", unsafe_allow_html=True)

def chat_interface():
    st.markdown('<h1 class="main-header">QueryCortex AI</h1>', unsafe_allow_html=True)
    
    # 1. Mode Selection
    mode = st.radio(
        "Select Engine", 
        ["🤖 Agent (Hybrid)", "🛢️ Database Only", "📜 Documents Only"], 
        horizontal=True,
        help="🤖 Agent: Best for complex queries across all data. \n\n"
             "🛢️ Database: Direct SQL generation and execution. \n\n"
             "📜 Documents: Semantic search through your uploaded PDFs."
    )
    
    clean_mode = mode.split(" ", 1)[1] # Removes the emoji for logic checks

    # 2. Chat History Display
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar="🧠" if msg["role"] == "assistant" else "👤"):
            # Always display the main content
            st.markdown(msg["content"])
            
            # Display additional metadata if it exists (Only for assistant)
            if msg["role"] == "assistant":
                if msg.get("thoughts"):
                    with st.expander("🧠 View Agent Thinking Process"):
                        st.markdown(msg["thoughts"])
                
                if msg.get("sql"):
                    with st.expander("🔍 View SQL Query"):
                        st.code(msg["sql"], language="sql")

                if msg.get("doc_references"):
                    with st.expander("📚 View References / Sources"):
                        st.markdown(msg["doc_references"])

    # 3. Chat Input & API Call
    if prompt := st.chat_input(f"Querying {clean_mode}..."):
        # Append User Message to History & Display
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Endpoint Mapping
        endpoint_map = {
            "Agent (Hybrid)": "/agent/query",
            "Database Only": "/db/query",
            "Documents Only": "/documents/query"
        }
        
        with st.chat_message("assistant", avatar="🧠"):
            with st.spinner("Thinking..."):
                resp = api_request("POST", endpoint_map[clean_mode], json_data={"query": prompt})
                
                if resp and resp.status_code == 200:
                    data = resp.json().get("data", {})
                    
                    # Initialize variables safely
                    answer = ""
                    sql = None
                    thoughts = None
                    refs = None

                    # --- Extract Data based on Mode ---
                    if clean_mode == "Database Only":
                        # db_query.py returns: natural_language_response, sql_query
                        answer = data.get("natural_language_response", "No response generated.")
                        sql = data.get("sql_query")
                    
                    elif clean_mode == "Agent (Hybrid)":
                        # llm_agent.py returns: answer, thoughts
                        answer = data.get("response", "No answer provided.") # FIXED: Matches llm_agent.py return key
                        thoughts = data.get("thoughts")
                    
                    elif clean_mode == "Documents Only":
                        # document queries usually return 'response' and optional 'doc_references'
                        answer = data.get("response", "No response found.")
                        refs = data.get("doc_references")

                    # --- Display Response ---
                    st.markdown(answer)
                    
                    if thoughts:
                        with st.expander("🧠 View Agent Thinking Process"):
                            st.markdown(thoughts)
                    
                    if sql:
                        with st.expander("🔍 View SQL Query"):
                            st.code(sql, language="sql")
                            
                    if refs:
                        with st.expander("📚 View References / Sources"):
                            st.markdown(refs)
                    
                    # --- Save to History ---
                    st.session_state.chat_history.append({
                        "role": "assistant", 
                        "content": answer, 
                        "sql": sql,
                        "thoughts": thoughts,
                        "doc_references": refs
                    })
                    
                elif resp:
                    error_msg = resp.json().get('detail', 'Processing Error')
                    st.error(f"❌ {error_msg}")
                    
# --- Main Logic ---
if not st.session_state.token:
    login_view()
else:
    if not st.session_state.active_docs: update_active_session()
    if not st.session_state.db_sessions: update_db_sessions()
    sidebar_view()
    chat_interface()
