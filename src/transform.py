import numpy as np
import pandas as pd
from pathlib import Path

def transformar_dados(dados_extraidos: Path) -> pd.DataFrame:
    # Percorrer a pasta de ano
    dataframes = []
    for sub_diretorio in dados_extraidos.iterdir():
        ano = sub_diretorio.name
        if sub_diretorio.is_dir():
            # Percorrer cada arquivo e leitura de cada CSV
            for arquivo_csv in sub_diretorio.glob("*.csv"):
                df = pd.read_csv(
                    arquivo_csv,
                    sep=";",
                    skiprows=3,
                    encoding="latin-1",
                    decimal=",",
                    thousands='.',
                )
                
                # Enriquecimento do DataFrame
                df["Ano"] = ano
                df["Tipo Conta"] = np.select(
                    [
                        df["Conta"].str.match(r"^\d{2} "),
                        df["Conta"].str.contains(r"\.", regex=True)
                    ],
                    [
                        "Função",
                        "Subfunção"
                    ],
                    default=None
                )

                # Filtro de colunas 
                df = df[(df["Coluna"].isin(["Despesas Empenhadas", "Despesas Pagas"])) & (df["Tipo Conta"].notnull())]

                # Garantindo que valor esteja formatado em número
                df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
                dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)