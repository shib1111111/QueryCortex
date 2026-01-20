# 🧠 QueryCortex

**QueryCortex** is a production-grade, agentic AI platform designed for intelligent reasoning over **structured databases** and **unstructured document corpora**. It combines **LLM-driven planning**, **Retrieval-Augmented Generation (RAG)**, and **secure backend engineering** to dynamically route queries across SQL databases and vector stores, delivering accurate and context-aware responses.

> 🚀 Built for real-world systems where data lives across databases, documents, and roles.

---

## 🗺️ System Architecture

<p align="center">
  <img src="documentation/llm_agent arc.png" alt="QueryCortex Architecture" width="90%" />
</p>

The architecture illustrates how **QueryCortex plans, routes, and executes queries** using an agentic decision layer that chooses between:

* 📄 *Document-first retrieval* (Vector Search)
* 🗄️ *Database-first execution* (SQL)
* 🔁 *Multi-step hybrid reasoning*

---

## ✨ Key Features

### 🔐 Secure Authentication & Sessions

* OAuth2-based login with **JWT tokens** (30-minute expiration)
* Secure logout with session invalidation
* Persistent session tracking with expiration handling

### 👥 Role-Based Access Control (RBAC)

* Fine-grained access to documents and queries based on user roles
* Role-specific default documents via `ROLE_PDFS`
* Strong isolation between user data

### 📄 Intelligent Document Management

* Upload and process **PDF documents** per role
* Automatic ingestion into **vector stores**
* Startup processing of default role documents

### 🧠 Agentic Query Processing

* **Query Agent** plans execution using intent + strategy detection
* Dynamically selects:

  * 🗄️ Database Query (SQL)
  * 📄 Document Query (Vector Search)
  * 🔄 Hybrid multi-step execution
* Completion checks ensure accurate and complete answers

### 📊 Database Integration

* PostgreSQL backend with **SQLAlchemy ORM**
* Automatic schema introspection
* Safe query execution with natural language responses

### 🧾 Logging & Observability

* Detailed query history with execution time
* Login metadata logging (IP, OS, browser, device)
* Safe logging (no secrets exposed)

### 🌍 Timezone-Aware System

* All timestamps stored in **Asia/Kolkata** timezone
* Migration support for offset-naive records

---

## 🏗️ Technology Stack (Tooling)

| Layer             | Tools                        |
| ----------------- | ---------------------------- |
| Backend API       | FastAPI 🧩                   |
| Authentication    | OAuth2 · JWT 🔐              |
| Database          | PostgreSQL · SQLAlchemy 🗄️  |
| Document Search   | Vector Stores · RAG 📄       |
| LLM Orchestration | Agent-based Planning 🤖      |
| Frontend          | Vue 3 · Vite · TypeScript 🎨 |
| Security          | CORS · RBAC · Bcrypt 🛡️     |

---

## 📦 Prerequisites

* **Python** ≥ 3.8
* **PostgreSQL** ≥ 12
* **Node.js** (Vite-compatible)
* **npm / pnpm**

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shib1111111/QueryCortex
cd QueryCortex
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Frontend

```bash
cd frontend
npm install
```

---

## 🔧 Configuration

### Backend `.env` (server root)

```env
DB_URI=postgresql://username:password@localhost:5432/querycortex
JWT_SECRET_KEY=your-secret-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Frontend `.env` (frontend root)

```env
VITE_BASE_URL=http://localhost:8080
```

📌 **Notes**:

* Generate JWT secret using: `os.urandom(32).hex()`
* Default documents are auto-loaded via `ROLE_PDFS`

---

## ▶️ Running the Application

### Start Backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

➡️ API: [http://localhost:8080](http://localhost:8080)

### Start Frontend

```bash
cd frontend
npm run dev
```

➡️ UI: [http://localhost:5173](http://localhost:5173)

---

## 🗄️ Database Schema Overview

* **User** – account & role details
* **UserSession** – token lifecycle & expiry
* **UserLog** – login environment metadata
* **Documents** – uploaded & default PDFs
* **ChatHistory** – queries, responses & timing

---

## 📄 Document Processing Flow

1. PDFs uploaded per role
2. Stored at `ROOT_DIR/dataset/pdfs/<role>`
3. Converted into vector embeddings
4. Queried via semantic search during agent execution

---

## 🔐 Security Highlights

* JWT-protected endpoints
* Password hashing with bcrypt
* Strict CORS policies
* Automatic session cleanup
* No sensitive data in logs

---

## 🎥 Video Walkthroughs

* **AI Agent Architecture**
  [https://youtu.be/mWcpJCHRmog](https://youtu.be/mWcpJCHRmog)

* **End-to-End Demo**
  [https://youtu.be/E_-fb--rXds](https://youtu.be/E_-fb--rXds)

---

## 📜 License

Licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 📬 Contact

**Shib Kumar**
📧 [shibkumarsaraf05@gmail.com](mailto:shibkumarsaraf05@gmail.com)
🐙 GitHub: [https://github.com/shib1111111](https://github.com/shib1111111)

---

> ⭐ If you find QueryCortex useful, consider starring the repo!
