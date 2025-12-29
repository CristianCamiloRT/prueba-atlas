from typing import List
from sqlalchemy import text
from sqlalchemy.engine import Engine

from .schemas import SalesByCategory


def fetch_sales_by_category(engine: Engine) -> List[SalesByCategory]:
    sql = text("""
        SELECT
            pp.id_producto AS id_producto,
            pp.categoria AS categoria,
            SUM(vv.cantidad) AS total_unidades,
            SUM(vv.cantidad * pp.precio) AS total_ventas
        FROM ventas vv
        LEFT JOIN productos pp ON vv.id_producto = pp.id_producto
        GROUP BY pp.id_producto
        ORDER BY total_ventas DESC;
    """)

    with engine.connect() as conn:
        rows = conn.execute(sql).mappings().all()

    return [
        SalesByCategory(
            id_producto=row["id_producto"],
            categoria=row["categoria"],
            total_unidades=int(row["total_unidades"] or 0),
            total_ventas=float(row["total_ventas"] or 0),
        )
        for row in rows
    ]