# Prueba de Conocimiento

Este repositorio contiene la solución completa del ejercicio:

1) **Base de datos MySQL**: tablas `clientes`, `productos`, `ventas` + datos  
2) **Consultas SQL** requeridas + **VIEW**  
3) **ETL en Python**: extrae desde BD origen y carga en BD destino 
4) **API en Python (FastAPI)**: endpoint JSON total ventas por categoría  
5) **Power BI**: dashboard con los 3 visuales solicitados  

---

# PASO A PASO COMPLETO (Ejecución / Despliegue)

> **Orden recomendado:** 1) MySQL → 2) ETL → 3) API → 4) Power BI

---

## 1) Base de Datos MySQL (Schema + Seeds + Queries + View)

### 1.1 Ejecutar schema (crear BD y tablas)
Desde la **raíz del repo**:

**Windows (CMD)**
```bat
cd /d "RUTA\A\TU\REPO"
```

**Linux/Mac**
```bash
cd "RUTA/A/TU/REPO"
```

Ejecuta el schema con MySQL CLI:

- Si tu root tiene password:
```bash
mysql -u root -p < sql/1_schema.sql
```

- Si tu password es vacío:
```bash
mysql -u root < sql/1_schema.sql
```

> Si usas otro puerto/host:
> `mysql -h 127.0.0.1 -P 3306 -u root -p < sql/01_schema.sql`

### 1.2 Ejecutar seeds (insertar datos)
- Con password:
```bash
mysql -u root -p < sql/2_seeds.sql
```

- Password vacío:
```bash
mysql -u root < sql/2_seeds.sql
```

### 1.3 Ejecutar consultas requeridas
```bash
mysql -u root -p < sql/3_queries.sql
```

### 1.4 Crear la VIEW requerida
```bash
mysql -u root -p < sql/4_views.sql
```

---

## 2) ETL (Python) — BD Origen → BD Destino

El ETL conecta a:
- **Origen:** `prueba_ventas`
- **Destino:** `prueba_ventas_dest` (o db que desees)

y carga las tablas:
- `clientes`, `productos`, `ventas`

> El ETL usa su propio entorno virtual: `etl/.venv`

### 2.1 Entrar a la carpeta ETL
```bat
cd /d "RUTA\A\TU\REPO\etl"
```

### 2.2 Crear y activar venv (ETL)

**Windows CMD**
```bat
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2.3 Instalar dependencias (ETL)
```bash
pip install -r requirements.txt
```

### 2.4 Crear archivos de configuración (ETL)
Copia los archivos ejemplo:

**Windows CMD**
```bat
copy config.example.yml config.yml
copy .env.example .env
```

**Linux/Mac**
```bash
cp config.example.yml config.yml
cp .env.example .env
```

Edita `etl/.env`:
- Si el password es vacío:
```env
SRC_DB_PASSWORD=''
DST_DB_PASSWORD=''
```

Edita `etl/config.yml` (ejemplo recomendado):
```yml
source:
  host: "127.0.0.1"
  port: 3306
  user: "root"
  password_env: "SRC_DB_PASSWORD"
  database: "prueba_ventas"

destination:
  host: "127.0.0.1"
  port: 3306
  user: "root"
  password_env: "DST_DB_PASSWORD"
  database: "prueba_ventas_dest"

etl:
  truncate_before_load: true # (true si las tablas ya existen en la db de origen y quieres truncarlas)
```

### 2.5 Ejecutar ETL
Asegúrate de estar dentro de `etl/` y con venv activo:

```bash
python -m src.main
```

Salida esperada (aprox):
- Truncando destino...
- Extrayendo...
- Transformando...
- Cargando...
- ETL OK...

---

## 3) API (FastAPI) — Endpoint JSON

La API expone:

- `GET /ventas/por-categoria` → total de ventas por categoría

> La API usa su propio entorno virtual: `api/.venv`

### 3.1 Entrar a la carpeta API
```bat
cd /d "RUTA\A\TU\REPO\api"
```

### 3.2 Crear y activar venv (API)

**Windows CMD**
```bat
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.3 Instalar dependencias (API)
```bash
pip install -r requirements.txt
```

### 3.4 Configurar variables de entorno (API)
Copia el ejemplo y edítalo:

**Windows CMD**
```bat
copy .env.example .env
```

**Linux/Mac**
```bash
cp .env.example .env
```

Edita `api/.env` para conectar a la BD destino del ETL:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=prueba_ventas_dest
```

### 3.5 Ejecutar la API
Asegúrate de estar dentro de `api/` con venv activo:

```bash
python -m uvicorn src.main:app --reload --port 8000
```

### 3.6 Acceder a las URLs del API
- **Swagger UI (Docs)**:  
  http://127.0.0.1:8000/docs

- **Endpoint JSON**:  
  http://127.0.0.1:8000/ventas/por-categoria

Ejemplo de respuesta:
```json
  [
    {"id_producto":1,"categoria":"Electrónica","total_unidades":6,"total_ventas":3000.0},
    {"id_producto":2,"categoria":"Electrónica","total_unidades":1,"total_ventas":1500.0},
    {"id_producto":3,"categoria":"Hogar","total_unidades":4,"total_ventas":800.0},
    {"id_producto":5,"categoria":"Ropa","total_unidades":4,"total_ventas":400.0}
  ]
```

---

## 4) Power BI (BI)
Se encuentra el archivo `dashboard.pbix`, dentro de la carpeta  `PowerBI`:

---

## Orden recomendado de ejecución (resumen)
1) `sql/1_schema.sql`
2) `sql/2_seeds.sql`
3) Ejecutar ETL: `cd etl && python -m src.main`
4) Ejecutar API: `cd api && python -m uvicorn src.main:app --reload --port 8000`
