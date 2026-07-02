from pathlib import Path

import pandas as pd

from src.extract import extrair_dados
from src.transform import transformar_dados


def main():
    origem = Path('dados_compactos')
    destino = Path('dados_extraidos')

    extrair_dados(origem, destino)
    df = transformar_dados(destino)

    # Validando o dataframe
    pd.set_option('display.max_columns', None)
    print(df.head())
    print(df.info())

if __name__ == "__main__":
    main()