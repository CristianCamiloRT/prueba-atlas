import pandas as pd
from sqlalchemy.engine import Engine

def extract_table(engine: Engine, table_name: str) -> pd.DataFrame:
    return pd.read_sql(f"SELECT * FROM {table_name};", con=engine)