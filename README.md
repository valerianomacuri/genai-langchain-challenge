# Knowledge Assistant (FastAPI + LangChain + RAG + ChromaDB + Prompt Engineering)

**Knowledge Assistant** es una **REST API** para búsqueda inteligente y respuesta a preguntas sobre documentos. Construida con **FastAPI**, **LangChain**, **RAG**, y **ChromaDB**, aprovecha **OpenAI LLMs** con **prompt engineering** para entregar respuestas precisas y contextuales.

---

## 🚀 Requisitos

* Python 3.11+
* uv instalado

```bash
pip install uv
```

---

## 📥 Clonar el repositorio

```bash
git clone https://github.com/valerianomacuri/knowledge-assistant.git
cd knowledge-assistant
```

---

## 📦 Instalar dependencias

```bash
uv sync
```

> Esto instala todas las dependencias desde `pyproject.toml` y crea el entorno virtual automáticamente.

---

## ▶️ Ejecutar en desarrollo

```bash
uv run uvicorn app.main:app --reload
```

* API: `http://localhost:8000`
* Documentación interactiva: `http://localhost:8000/docs`

---

## 🚀 Ejecutar en producción

```bash
uv run gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

---

## 🎨 Formatear código con Black

```bash
uv run black .
```

---

## 🗂️ Estructura del proyecto

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

## ✅ Stack tecnológico

* **FastAPI** → Framework API rápido y moderno
* **LangChain** → Gestión de chains y RAG
* **OpenAI** → LLMs para generación de respuestas
* **ChromaDB** → Vector database para embeddings
* **Prompt Engineering** → Optimización de prompts para respuestas más precisas
* **uv** → Gestor de dependencias
* **Uvicorn** → Servidor ASGI para desarrollo
* **Gunicorn** → Servidor WSGI para producción
* **Black** → Formateo automático de código

---

## 📄 Licencia

MIT
