# FastAPI Scaffolding (uv + uvicorn + gunicorn + black)

Scaffolding mínimo y listo para producción para construir APIs con **FastAPI**, usando **uv** como gestor de dependencias, **Uvicorn** para desarrollo, **Gunicorn** para producción y **Black** para formateo de código.

---

## 🚀 Requisitos

- Python 3.11+
- uv instalado

```bash
pip install uv
````

---

## 📥 Clonar el repositorio

```bash
git clone https://github.com/valerianomacuri/fastapi-scaffolding.git
cd fastapi-scaffolding
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
* Documentación: `http://localhost:8000/docs`

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
.
├── app/
│   └── main.py
├── pyproject.toml
└── .venv/
```

---

## ✅ Stack tecnológico

* FastAPI → Framework API
* uv → Gestor de dependencias
* Uvicorn → Servidor ASGI para desarrollo
* Gunicorn → Servidor WSGI para producción
* Black → Formateo automático de código

---

## 📄 Licencia

MIT
