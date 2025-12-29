from pydantic import BaseModel, Field

class SalesByCategory(BaseModel):
    id_producto: int = Field(..., examples=[1])
    categoria: str = Field(..., examples=["Electrónica"])
    total_unidades: int = Field(..., examples=[6])
    total_ventas: float = Field(..., examples=[3500.00])