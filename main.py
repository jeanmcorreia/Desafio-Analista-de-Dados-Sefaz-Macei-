from pathlib import Path

from src.load import carregar_dados
from src.extract import extrair_dados
from src.transform import transformar_dados

def main():
    origem = Path('dados_compactos')
    destino = Path('dados_extraidos')
    destino_processados = Path('dados_processados')

    extrair_dados(origem, destino)
    df = transformar_dados(destino)
    carregar_dados(df, destino_processados)

if __name__ == "__main__":
    main()