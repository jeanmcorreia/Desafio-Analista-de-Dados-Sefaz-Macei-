from pathlib import Path
import pandas as pd

def carregar_dados(data_frame: pd.DataFrame, destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    data_frame.to_parquet(destino / 'finbra_consolidado.parquet', index=False)