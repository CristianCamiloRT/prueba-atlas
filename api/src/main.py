from fastapi import FastAPI
from .db import get_engine
from .repository import fetch_sales_by_category
from .schemas import SalesByCategory

app = FastAPI(title="Prueba Ventas API", version="1.0.0")

_engine = get_engine()


@app.get("/ventas/por-categoria", response_model=list[SalesByCategory])
def sales_by_category():
    return fetch_sales_by_category(_engine)