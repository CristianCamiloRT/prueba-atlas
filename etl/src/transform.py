import pandas as pd

def transform_clientes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"]).dt.date
    return df

def transform_productos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["precio"] = pd.to_numeric(df["precio"])
    return df

def transform_ventas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"]).dt.date
    df["cantidad"] = pd.to_numeric(df["cantidad"]).astype("int64")
    return df