import os

# ## RENAME FILES WITH START ...

# # Diretório onde os arquivos estão localizados
# diretorio = '/home/jamilzin1/Downloads/music/'


# # Listar arquivos do dir
# arquivos = os.listdir(diretorio)

# # Percorre cada arquivo
# for arquivo in arquivos:
#     if arquivo.startswith('[SPOTIFY-DOWNLOADER.COM] '):
#         novo_nome = arquivo.replace('[SPOTIFY-DOWNLOADER.COM] ', '')
#         antigo_caminho = os.path.join(diretorio, arquivo)
#         novo_caminho = os.path.join(diretorio, novo_nome)
        
#         # Renomeia o arquivo
#         os.rename(antigo_caminho, novo_caminho)
#         print(f"Arquivo {arquivo} renomeado para {novo_nome}")



# CONCATENAR NOME DE ARQUIVOS 

# Diretório onde os arquivos estão localizados
diretorio = '/home/jamilzin1/Downloads/music/teste/'

count = 0

# Listar arquivos do dir
# arquivos = os.listdir(diretorio) # se quiser ordenar em ordem alfabetica utilizar funçao 'sorted(arg)'
arquivos = sorted(os.listdir(diretorio))
# Percorre cada arquivo
for arquivo in arquivos:
   
    novo_nome = f"{count} - {arquivo}"
    antigo_caminho = os.path.join(diretorio, arquivo)
    novo_caminho = os.path.join(diretorio, novo_nome)
    
    # Renomeia o arquivo
    os.rename(antigo_caminho, novo_caminho)
    count+=1
    print(f"Arquivo {arquivo} renomeado para {novo_nome}")



