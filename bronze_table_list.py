# Databricks notebook source
#lendo todos os dados e filtrando dados unicos
df =spark.read.json("dbfs:/Volumes/raw/pokemon")
df.distinct().show()
df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS bronze
# MAGIC

# COMMAND ----------

# Lê os arquivos JSON do diretório
df = spark.read.json("dbfs:/Volumes/raw/pokemon/")

# Define o caminho para a tabela Delta
delta_table_path = "dbfs:/mnt/delta/bronze/pokemon_list"

# Transforma os dados, remove duplicatas e escreve na tabela Delta
df.distinct() \
  .coalesce(1) \
  .write \
  .format("delta") \
  .mode("overwrite") \
 .saveAsTable("bronze.pokemon_list")

print(f"Dados salvos no diretório Delta: {delta_table_path}")



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.pokemon_list
# MAGIC
# MAGIC
# MAGIC
