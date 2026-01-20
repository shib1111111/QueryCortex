# 🧠 QueryCortex

### An Agentic AI Platform for Deep Reasoning over Data & Documents

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Agentic_AI-Deep_Reasoning-6A5ACD?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Semantic_Vector_Search-FF6F00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

## 🚀 Overview

**QueryCortex** is a **production-grade agentic AI orchestration platform** designed to perform **deep reasoning, intent understanding, and autonomous decision-making** across:

- 📊 **Structured data** (SQL databases)
- 📄 **Unstructured knowledge** (PDFs, documents)
- 🔐 **Role-aware enterprise environments**

Unlike traditional chatbots, QueryCortex **thinks before it answers**.  
It plans execution paths, validates reasoning, selects tools dynamically, and ensures responses are **complete, explainable, and safe**.

> 💡 Built for real-world systems where AI must operate across data silos, security boundaries, and business logic.

---

## 📑 Table of Contents

- [System Architecture](#system-architecture)
- [Core Capabilities](#core-capabilities)
- [Agentic Intelligence Layer](#agentic-intelligence-layer)
- [Database Intelligence](#database-intelligence)
- [Observability & Auditability](#observability--auditability)
- [Timezone Handling](#timezone-handling)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Database Schema Overview](#database-schema-overview)
- [Document Processing Pipeline](#document-processing-pipeline)
- [Security & Compliance](#security--compliance)
- [Video Walkthroughs](#video-walkthroughs)
- [License](#license)
- [Contact](#contact)

---

<a id="system-architecture"></a>
## 🗺️ System Architecture

<p align="center">
  <img src="./documentation/llm_agent arc.png" alt="QueryCortex Architecture" width="90%" />
</p>

QueryCortex uses a **multi-agent reasoning architecture** where each user query flows through an **intelligent decision layer**.

Depending on intent and context, the system dynamically selects:

- 📄 **Semantic document reasoning** (Vector-based RAG)
- 🗄️ **Schema-aware SQL execution**
- 🔁 **Hybrid multi-hop reasoning pipelines**

This ensures **transparent, auditable AI workflows**, not black-box responses.

---

<a id="core-capabilities"></a>
## ✨ Core Capabilities

### 🔐 Secure Authentication & Stateful Sessions
- OAuth2-compliant authentication
- JWT-based access tokens (30-minute expiry)
- Secure logout with server-side invalidation
- Full session lifecycle tracking

### 👥 Role-Based Access Control (RBAC)
- Fine-grained authorization at **query & document level**
- Role-scoped default knowledge bases via `ROLE_PDFS`
- Strict isolation between roles and datasets

### 📄 Intelligent Document Intelligence (NLP + RAG)
- Role-aware PDF ingestion
- Semantic chunking and embeddings
- High-recall vector search with grounding
- Auto-loading of default documents at startup

---

<a id="agentic-intelligence-layer"></a>
## 🧠 Agentic Intelligence Layer

QueryCortex is **not a simple chatbot** — it is an **agent-driven reasoning system**.

### 🧩 Core Agents

- **Intent Detection Agent**
  - Deep NLP-based intent classification
  - Distinguishes analytical, informational, and operational queries

- **Auto-Thinking Planning Agent**
  - Decomposes complex queries into steps
  - Plans optimal execution order

- **Routing & Strategy Agent**
  - Selects SQL, RAG, or Hybrid execution
  - Prevents unsafe or invalid query paths

- **Query Completion Checker**
  - Ensures answers are complete and grounded
  - Prevents hallucinations and partial responses

- **Reasoning Validator**
  - Verifies alignment between intent, execution, and output

---

<a id="database-intelligence"></a>
## 📊 Database Intelligence

- PostgreSQL-backed persistence layer
- SQLAlchemy ORM with schema introspection
- Safe, explainable SQL execution
- Natural-language-to-SQL reasoning with result interpretation

---

<a id="observability--auditability"></a>
## 🧾 Observability & Auditability

- Full query execution history
- Latency and execution-time metrics
- Login metadata capture (IP, OS, browser, device)
- Secure logging with **zero secret exposure**

---

<a id="timezone-handling"></a>
## 🌍 Timezone Handling

- All timestamps standardized to **Asia/Kolkata**
- Automatic handling of legacy offset-naive records

---

<a id="technology-stack"></a>
## 🏗️ Technology Stack

| Layer          | Technologies                            |
|----------------|------------------------------------------|
| Backend API    | FastAPI                                  |
| Authentication | OAuth2 · JWT                             |
| Database       | PostgreSQL · SQLAlchemy                  |
| NLP & RAG      | Vector Stores · Semantic Search          |
| Agentic AI     | Planning Agents · Reasoning Agents       |
| Frontend       | Vue 3 · Vite · TypeScript                |
| Security       | RBAC · CORS · Bcrypt                     |

---

<a id="prerequisites"></a>
## 📦 Prerequisites

- **Python** ≥ 3.8  
- **PostgreSQL** ≥ 12  
- **Node.js** (Vite compatible)  
- **npm / pnpm**

---

<a id="installation"></a>
## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/shib1111111/QueryCortex
cd QueryCortex
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Frontend Setup

```bash
cd frontend
npm install
```

---

<a id="configuration"></a>

## 🔧 Configuration

### Backend `.env`

```env
DB_URI=postgresql://username:password@localhost:5432/querycortex
JWT_SECRET_KEY=your-secret-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Frontend `.env`

```env
VITE_BASE_URL=http://localhost:8080
```

**Best Practices**

* Generate JWT secret using: `os.urandom(32).hex()`
* Default role documents auto-load via `ROLE_PDFS`

---

<a id="running-the-application"></a>

## ▶️ Running the Application

### Backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

➡ API: [http://localhost:8080](http://localhost:8080)

### Frontend

```bash
cd frontend
npm run dev
```

➡ UI: [http://localhost:5173](http://localhost:5173)

---

<a id="database-schema-overview"></a>

## 🗄️ Database Schema Overview

* **User** – identity and role metadata
* **UserSession** – token lifecycle management
* **UserLog** – authentication environment data
* **Documents** – role-based PDFs
* **ChatHistory** – reasoning trace & timing

---

<a id="document-processing-pipeline"></a>

## 📄 Document Processing Pipeline

1. Role-based PDF upload
2. Secure storage at `ROOT_DIR/dataset/pdfs/<role>`
3. Embedding generation
4. Semantic retrieval during agent execution

---

<a id="security--compliance"></a>

## 🔐 Security & Compliance

* JWT-secured endpoints
* Bcrypt password hashing
* Strict CORS enforcement
* Automatic session expiration
* No sensitive data in logs

---

<a id="video-walkthroughs"></a>

## 🎥 Video Walkthroughs

* **Agentic AI Architecture**
  [https://youtu.be/mWcpJCHRmog](https://youtu.be/mWcpJCHRmog)

* **End-to-End System Demo**
  [https://youtu.be/E_-fb--rXds](https://youtu.be/E_-fb--rXds)

---

<a id="license"></a>

## 📜 License

Released under the **MIT License**.
See [LICENSE](LICENSE) for details.

---

<a id="contact"></a>

## 📬 Contact

**Shib Kumar**
📧 [shibkumarsaraf05@gmail.com](mailto:shibkumarsaraf05@gmail.com)
🐙 GitHub: [https://github.com/shib1111111](https://github.com/shib1111111)

---

⭐ *If QueryCortex aligns with your vision for intelligent systems, consider starring the repository.*
