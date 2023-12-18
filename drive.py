import gdown
import zipfile
import os

# Substitua 'LINK_DO_DRIVE' pelo link correto do Google Drive
link_do_drive_correto = 'https://drive.google.com/uc?id=1_41_ehQko3JpNkJms0kScJnykXYLgscF'
FONTES_PROJETO = r'C:\CSMP2_APP'
# Substitua 'NOME_DO_ARQUIVO_LOCAL' pelo caminho completo do arquivo local
# Certifique-se de incluir a extensão correta do arquivo (por exemplo, '.zip')
nome_do_arquivo_local = FONTES_PROJETO + '\dw.zip'
os.makedirs(FONTES_PROJETO, exist_ok=True)

# Se o arquivo ZIP existir, exclua-o
if os.path.exists(nome_do_arquivo_local):
    os.remove(nome_do_arquivo_local)

# Faça o download do arquivo ZIP
gdown.download(link_do_drive_correto, nome_do_arquivo_local, quiet=False)
# Descompactar arquivo:
diretorio_extracao = FONTES_PROJETO + '\\arquivo'
os.makedirs(diretorio_extracao, exist_ok=True)

# Abra o arquivo zip
with zipfile.ZipFile(nome_do_arquivo_local, 'r') as zip_ref:
    # Extraia todos os arquivos para o diretório de extração
    zip_ref.extractall(diretorio_extracao)

print(f"Arquivo {nome_do_arquivo_local} descompactado em {diretorio_extracao}.")