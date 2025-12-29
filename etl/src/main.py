import logging
from time import perf_counter
from pathlib import Path

from .config import load_config
from .db import make_engine, ensure_database_exists, create_schema_if_not_exists, truncate_tables
from .extract import extract_table
from .transform import transform_clientes, transform_productos, transform_ventas
from .load import load_table


def setup_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def main() -> None:
    setup_logging()

    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "config.yml"

    cfg = load_config(str(config_path))
    t0 = perf_counter()

    src_engine = make_engine(cfg.source, with_db=True)

    dst_server_engine = make_engine(cfg.destination, with_db=False)
    ensure_database_exists(dst_server_engine, cfg.destination.database)

    dst_engine = make_engine(cfg.destination, with_db=True)
    create_schema_if_not_exists(dst_engine)

    if cfg.etl.truncate_before_load:
        logging.info("Truncando destino...")
        truncate_tables(dst_engine)

    logging.info("Extrayendo origen...")
    df_clientes = extract_table(src_engine, "clientes")
    df_productos = extract_table(src_engine, "productos")
    df_ventas = extract_table(src_engine, "ventas")

    logging.info("Transformando...")
    df_clientes = transform_clientes(df_clientes)
    df_productos = transform_productos(df_productos)
    df_ventas = transform_ventas(df_ventas)

    logging.info("Cargando destino...")
    n1 = load_table(df_clientes, dst_engine, "clientes")
    n2 = load_table(df_productos, dst_engine, "productos")
    n3 = load_table(df_ventas, dst_engine, "ventas")

    dt = perf_counter() - t0
    logging.info(f"ETL OK | clientes={n1} productos={n2} ventas={n3} | tiempo ejecución = {dt:.2f}s")


if __name__ == "__main__":
    main()