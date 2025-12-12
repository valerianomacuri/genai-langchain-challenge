# Knowledge Assistant (FastAPI + LangChain + RAG + ChromaDB + Prompt Engineering)

**Knowledge Assistant** is a **REST API** for intelligent document search and question-answering. Built with **FastAPI**, **LangChain**, **RAG**, and **ChromaDB**, it leverages **OpenAI LLMs** with **prompt engineering** to provide accurate, context-aware responses.

---

## 🚀 Requirements

* Python 3.11+
* `uv` installed

```bash
pip install uv
```

---

## 📥 Clone the repository

```bash
git clone https://github.com/valerianomacuri/knowledge-assistant.git
cd knowledge-assistant
```

---

## 📦 Install dependencies

```bash
uv sync
```

> This installs all dependencies from `pyproject.toml` and automatically creates a virtual environment.

---

## ▶️ Run in development

```bash
uv run uvicorn app.main:app --reload
```

* API: `http://localhost:8000`
* Interactive docs: `http://localhost:8000/docs`

---

## 🚀 Run in production

```bash
uv run gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

---

## 🎨 Format code with Black

```bash
uv run black .
```

---

## 🗂️ Project structure

```
knowledge-assistant/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   └── utils/
├── tests/
├── pyproject.toml
└── .venv/
```

---

## ✅ Technology Stack

* **FastAPI** → Modern and fast API framework
* **LangChain** → Chains and RAG management
* **OpenAI** → LLMs for response generation
* **ChromaDB** → Vector database for embeddings
* **Prompt Engineering** → Optimized prompts for more accurate answers
* **uv** → Dependency manager
* **Uvicorn** → ASGI server for development
* **Gunicorn** → WSGI server for production
* **Black** → Automatic code formatting

---

## 📄 License

MIT
