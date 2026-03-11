# Clase 6 — El problema de no testear

Recursos de la clase **"El problema de no testear — un escenario real"** del curso  
**Testing con Python desde la perspectiva de un dev**.

---

## ¿Qué hay en este directorio?

```
1-broken-code/
├── main.py           # API con los bugs que veremos en clase
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Este archivo
```

---

## Requisitos previos

- Python **3.10 o superior**
- Tener `pip` disponible en tu terminal

Para verificar tu versión de Python:

```bash
python --version
# o en algunos sistemas
python3 --version
```

---

## Cómo montar el ambiente

### 1. Crear el ambiente virtual

Un ambiente virtual aísla las dependencias de este proyecto
para que no interfieran con otros proyectos en tu máquina.

**En macOS / Linux:**
```bash
python3 -m venv venv
```

**En Windows:**
```bash
python -m venv venv
```

Esto crea una carpeta llamada `venv` en el directorio actual.

---

### 2. Activar el ambiente virtual

Este paso es importante — sin activarlo, las dependencias
se instalarán de forma global y no dentro del ambiente.

**En macOS / Linux:**
```bash
source venv/bin/activate
```

**En Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**En Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

Sabrás que está activo porque el nombre `(venv)` aparecerá
al inicio de tu línea de comandos, así:

```
(venv) $
```

---

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Levantar el servidor

```bash
uvicorn main:app --reload
```

Si todo está bien, verás algo como esto:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process using WatchFiles
```

---

## Probando los endpoints

Con el servidor corriendo, abre una segunda terminal y ejecuta los siguientes comandos.

> **Nota:** en Windows puedes usar PowerShell, Git Bash, o el cliente HTTP que prefieras.  
> También puedes usar la documentación interactiva en `http://localhost:8000/docs`.

---

### ✅ Caso 1 — Login exitoso

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "supersecret123"}'
```

**Respuesta esperada:**
```json
{
  "token": "token-john-abc123",
  "role": "admin"
}
```

---

### 🔴 Caso 2 — Usuario que no existe

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "noexiste", "password": "cualquiercosa"}'
```

**Respuesta esperada:**
```json
{
  "detail": "User noexiste not found. DB connection: postgresql://admin:supersecret123@prod-db.internal:5432/users"
}
```

---

### 🔴 Caso 3 — Payload malformado

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": 12345, "password": null}'
```

**Respuesta esperada:** un error 422 o 500 con información interna expuesta.

---

## Desactivar el ambiente virtual

Cuando termines, puedes desactivar el ambiente con:

```bash
deactivate
```

---

## ¿Algo no funciona?

Verifica que:

1. El ambiente virtual está **activado** — debe aparecer `(venv)` en tu terminal
2. Instalaste las dependencias **dentro del ambiente activado**
3. Estás ejecutando `uvicorn` desde el mismo directorio donde está `main.py`
4. El puerto `8000` no está ocupado por otro proceso — si lo está, puedes cambiar el puerto así:

```bash
uvicorn main:app --reload --port 8001
```