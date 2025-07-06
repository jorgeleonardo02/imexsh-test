# IMEXHS Device Management API

Este proyecto es una API construida con **FastAPI** para la gestión de dispositivos médicos y sus datos asociados. Usa **SQLAlchemy** para el ORM, **Alembic** para las migraciones y está configurado con **Poetry** como gestor de dependencias.

---

## 📦 Tecnologías utilizadas

- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Poetry](https://python-poetry.org/)

---

## 🚀 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/jorgeleonardo02/imexsh-test
cd IMEXHS_TEST/api
```

### 2. Crear entorno virtual manualmente con `venv`

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

- En **Linux/MacOS**:

```bash
source .venv/bin/activate
```

- En **Windows**:

```bash
.venv\Scripts\activate
```

### 4. Instalar Poetry (si no lo tienes)

```bash
pip install poetry
```

### 5. Instalar dependencias con Poetry

```bash
poetry install
```

---

## ⚙️ Variables de entorno

Crea un archivo `.env` en la raíz con las siguientes variables:

```env
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost:5432/nombre_bd
```

> Asegúrate de que esta URL coincida con la definida en tu `alembic.ini`.

---

## 📄 Migraciones con Alembic

### Crear una nueva revisión de migración

```bash
alembic revision --autogenerate -m "mensaje de la migración"
```

### Aplicar migraciones

```bash
alembic upgrade head
```

### Revertir última migración

```bash
alembic downgrade -1
```

---

## 🧪 Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

> Asegúrate de que tu archivo `main.py` esté dentro de `app/` y defina la variable `app = FastAPI()`.

---

## ✅ Comandos útiles

| Acción                      | Comando                                    |
|----------------------------|--------------------------------------------|
| Instalar dependencias      | `poetry install`                           |
| Activar entorno (Linux/Mac)| `source .venv/bin/activate`                |
| Activar entorno (Windows)  | `.venv\Scripts\activate`                 |
| Agregar nueva dependencia  | `poetry add <paquete>`                     |
| Crear revisión Alembic     | `alembic revision --autogenerate -m "msg"` |
| Ejecutar migraciones       | `alembic upgrade head`                     |

---


## 馃攲 Ejemplos de endpoints

### Obtener todos los grupos de dispositivos

```http
GET http://localhost:8081/device-groups/
```

#### Payload:

```json
{
  "3": {
    "id": "aabbcc3",
    "data": [
      "78 83 21 68 96 46 40 11 1 88",
      "58 75 71 69 33 14 15 93 18 54",
      "46 54 73 63 85 4 30 76 15 56"
    ],
    "deviceName": "CT SCAN1"
  },
  "4": {
    "id": "aabbcc4",
    "data": [
      "14 85 30 41 64 66 85 76 96 71",
      "68 53 85 9 35 52 68 0 17 5",
      "78 40 83 72 82 94 8 19 23 62"
    ],
    "deviceName": "CT SCAN2"
  }
}
```

### Obtener un grupo específico por ID:

```http
GET http://localhost:8081/device-groups/?id=4
```

### Actualizar información de un grupo de dispositivos

```http
PUT http://localhost:8081/device-groups/3/?new_id=aabbcc12&device_name=CT%20SCAN3
```

### Eliminar un grupo de dispositivos

```http
DELETE http://localhost:8081/device-groups/3
```

---
