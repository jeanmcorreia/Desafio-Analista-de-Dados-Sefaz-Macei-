from pathlib import Path
from src.extract import extrair_dados

def main():
    origem = Path('dados_compactos')
    destino = Path('dados_extraidos')

    extrair_dados(origem, destino)

if __name__ == "__main__":
    main()