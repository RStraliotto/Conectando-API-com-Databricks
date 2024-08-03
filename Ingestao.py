# Databricks notebook source
# Verificar o conteúdo do diretório para garantir que ele existe
try:
    files = dbutils.fs.ls("dbfs:/Volumes/raw/pokemon")
    print("Conteúdo do diretório /Volumes/raw/pokemon:")
    for file in files:
        print(file.path)
except Exception as e:
    print(f"Erro ao listar o diretório: {e}")


# COMMAND ----------

import requests
import datetime
import json
import io

# Define a URL da API
url = "https://pokeapi.co/api/v2/pokemon?limit=10"

# Faz a requisição GET para a API
resp = requests.get(url)

# Converte a resposta em formato JSON para um dicionário Python
data = resp.json()

# Obtém a data e hora atual no formato YYYYMMDD-HHMMSS
current_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Define o caminho base e o caminho completo do arquivo JSON
base_path = "dbfs:/Volumes/raw/pokemon"
full_path = f"{base_path}/pokemon_list_{current_date}.json"

# Converte o JSON em uma string para usar com dbutils.fs.put
json_data = json.dumps(data)

# Salva o JSON no arquivo usando dbutils.fs.put
try:
    dbutils.fs.put(full_path, json_data, overwrite=True)
    print(f"Arquivo salvo em: {full_path}")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")


# COMMAND ----------

dbutils.fs.ls("dbfs:/Volumes/raw/pokemon/")
