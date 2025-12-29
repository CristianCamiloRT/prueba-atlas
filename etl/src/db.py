from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from .config import DbConfig

def make_engine(cfg: DbConfig, with_db: bool = True) -> Engine:
    db_part = f"/{cfg.database}" if with_db else ""
    url = f"mysql+pymysql://{cfg.user}:{cfg.password}@{cfg.host}:{cfg.port}{db_part}?charset=utf8mb4"
    return create_engine(url, future=True, pool_pre_ping=True)

def ensure_database_exists(server_engine: Engine, db_name: str) -> None:
    with server_engine.begin() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))

def create_schema_if_not_exists(dst_engine: Engine) -> None:
    schema_sql = """
    CREATE TABLE IF NOT EXISTS clientes (
      id_cliente INT NOT NULL AUTO_INCREMENT,
      nombre VARCHAR(80) NOT NULL,
      ciudad VARCHAR(50) NOT NULL,
      fecha_registro DATE NOT NULL,
      PRIMARY KEY (id_cliente)
    );

    CREATE TABLE IF NOT EXISTS productos (
      id_producto INT NOT NULL AUTO_INCREMENT,
      categoria VARCHAR(50) NOT NULL,
      precio DECIMAL(10,2) NOT NULL,
      PRIMARY KEY (id_producto)
    );

    CREATE TABLE IF NOT EXISTS ventas (
      id_venta INT NOT NULL AUTO_INCREMENT,
      id_cliente INT NOT NULL,
      id_producto INT NOT NULL,
      fecha_venta DATE NOT NULL,
      cantidad INT NOT NULL,
      PRIMARY KEY (id_venta),
      INDEX idx_ventas_cliente_fecha (id_cliente, fecha_venta),
      INDEX idx_ventas_producto_fecha (id_producto, fecha_venta),
      FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente) ON UPDATE CASCADE ON DELETE RESTRICT,
      FOREIGN KEY (id_producto) REFERENCES productos (id_producto) ON UPDATE CASCADE ON DELETE RESTRICT
    );
    """
    with dst_engine.begin() as conn:
        for stmt in [s.strip() for s in schema_sql.split(";") if s.strip()]:
            conn.execute(text(stmt + ";"))

def truncate_tables(dst_engine: Engine) -> None:
    with dst_engine.begin() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
        conn.execute(text("TRUNCATE TABLE ventas;"))
        conn.execute(text("TRUNCATE TABLE clientes;"))
        conn.execute(text("TRUNCATE TABLE productos;"))
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))