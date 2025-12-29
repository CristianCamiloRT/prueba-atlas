import pandas as pd
from sqlalchemy.engine import Engine

def load_table(df: pd.DataFrame, dst_engine: Engine, table_name: str) -> int:
    if df.empty:
        return 0

    df.to_sql(
        name=table_name,
        con=dst_engine,
        if_exists="append",
        index=False,
        method="multi",
    )
    return len(df)