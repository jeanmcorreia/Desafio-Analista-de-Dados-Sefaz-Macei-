# Importação de Bibliotecas
from pathlib import Path
from zipfile import ZipFile

def extrair_dados():

    diretorio_origem_base = Path('../dados_compactos')
    diretorio_destino_base = Path('../dados_extraidos')

    for sub_diretorio in diretorio_origem_base.iterdir():
        if sub_diretorio.is_dir():
            ano = sub_diretorio.name
            diretorio_destino_atual = Path(f'{diretorio_destino_base}/{ano}')
            diretorio_destino_atual.mkdir(parents=True, exist_ok=True)

            for arquivo_zip in sub_diretorio.glob('*.zip'):
                with ZipFile(arquivo_zip) as zip_file:
                    zip_file.extractall(path=diretorio_destino_atual) # Descompacta e grava em 'dados_extraidos'

if __name__ == "__main__":
    extrair_dados()