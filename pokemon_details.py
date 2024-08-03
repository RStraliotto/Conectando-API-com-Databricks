# Databricks notebook source
# Supondo que 'results' seja uma coluna que contém 'url'
df = spark.table("bronze.pokemon_list")
urls = df.select("results").toPandas()["results"].tolist()
print(urls)


# COMMAND ----------

dbutils.fs.ls("dbfs:/Volumes/raw/pokemon")


# COMMAND ----------

# Verifique e crie o diretório se necessário
dbutils.fs.mkdirs("/Volumes/raw/pokemon_details/")




# COMMAND ----------

import datetime
import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def get_and_save(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/dbfs/Volumes/raw/pokemons_details/{data['id']}_{now}.json"  # Caminho corrigido

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filename, "w") as open_file:
            json.dump(data, open_file, indent=4)

        return f"Arquivo criado em: {filename}"
        
    except Exception as e:
        return f"Erro: {e}"

# Define a URL base e o intervalo de IDs
base_url = 'https://pokeapi.co/api/v2/pokemon/'
start_id = 10
end_id = 20

# Gera a lista de URLs
urls = [f'{base_url}{pokemon_id}/' for pokemon_id in range(start_id, end_id + 1)]

# Define o número de threads
num_threads = 5

# Armazenar as mensagens de saída
output_messages = []

# Processa URLs com ThreadPoolExecutor e tqdm
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(get_and_save, url) for url in urls]

    # Usar tqdm para mostrar o progresso
    for future in tqdm(as_completed(futures), total=len(futures)):
        output_messages.append(future.result())

# Exibir as mensagens de saída após a barra de progresso
for message in output_messages:
    print(message)

