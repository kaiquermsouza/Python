#!/usr/bin/env python
# coding: utf-8

# # Projeto Final: Automatização de Movimentação de Arquivos

# ## Especificação

# 
# Neste projeto, além de desenvolver um script Python que automatiza a tarefa de mover arquivos Excel processados para um diretório específico, vamos expandir a funcionalidade para criar um dicionário contendo informações adicionais sobre os arquivos. Este dicionário terá o nome do arquivo como chave e uma lista com data de criação e tamanho como valor.
#         

# ## Implementação

# In[1]:


import os
import shutil
import time


# In[2]:


# Diretório de origem (de onde os arquivos serão verificados e movidos)
diretorio_origem = "./relatorios"


# In[3]:


# Diretório de destino (para onde os arquivos serão movidos)
diretorio_destino = "./relatorios processados"


# In[4]:


# Verificando se o diretório de destino existe, senão, cria
if not os.path.exists(diretorio_destino):
    os.mkdir(diretorio_destino)


# In[5]:


# Listando todos os arquivos do diretório de origem
arquivos = os.listdir(diretorio_origem)


# In[6]:


# Dicionário para armazenar informações sobre os arquivos
info_arquivos = {}


# In[7]:


arquivos_processados = [arquivo for arquivo in arquivos if arquivo.endswith('_processado.xlsx')]

arquivos_processados


# In[8]:


for arquivo_processado in arquivos_processados:
    caminho_completo_origem = os.path.join(diretorio_origem, arquivo_processado)
    caminho_completo_destino = os.path.join(diretorio_destino, arquivo_processado)

    shutil.move(caminho_completo_origem, caminho_completo_destino)

    print(f'Arquivo {caminho_completo_origem} movido para {caminho_completo_destino}')


# In[9]:


# Vamos incrementar esse script, apresentando a data de criação de cada arquivo
for arquivo in arquivos_processados:
    caminho_completo = os.path.join(diretorio_destino, arquivo)

    # Obtendo informações sobre o arquivo
    tamanho = os.path.getsize(caminho_completo)
    data_criacao = time.ctime(os.path.getctime(caminho_completo))

    # Adicionando informações no dicionário
    info_arquivos[arquivo] = [data_criacao, tamanho]

info_arquivos


# In[10]:


info_arquivos['relatorio_0_processado.xlsx']


# In[12]:


print(f"Quantidade de arquivos movidos: {len(info_arquivos)}")


# In[ ]:




