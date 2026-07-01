# Importação de Bibliotecas
from pathlib import Path
from zipfile import ZipFile, BadZipFile

def extrair_dados(diretorio_origem_base: Path, diretorio_destino_base: Path) -> None:
    """
    Extrai todos os arquivos .zip presentes na pasta para o diretório de destino correspondente.
    """
    for sub_diretorio in diretorio_origem_base.iterdir():

       # Cria destino do arquivo
       if sub_diretorio.is_dir():
            diretorio_destino_atual = diretorio_destino_base / sub_diretorio.name
            diretorio_destino_atual.mkdir(parents=True, exist_ok=True)

            # Descompactação e gravação do arquivo
            for arquivo_zip in sub_diretorio.glob('*.zip'):
                try:
                    with ZipFile(arquivo_zip) as zip_file:
                        zip_file.extractall(path=diretorio_destino_atual)
                except BadZipeFile:
                    print(f"{arquivo.zip} está corrompido.")