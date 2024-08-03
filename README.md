# Conectando-API-com-Databricks
Exemplo Conectando a API em nosso Data Lakehouse e Orquestração das atividades via Workflow

# Projeto de Ingestão de Dados da API Pokémon

## Descrição

Este projeto visa a ingestão de dados da API Pokémon para um Data Lakehouse usando Databricks. Inclui a conexão com a API, armazenamento de dados no formato Delta, e criação de tabelas para análise de negócios. O projeto também demonstra o uso de técnicas de programação multithread e a biblioteca `tqdm` para visualização do progresso.

## Estrutura do Projeto

### 1. Conexão com a API em Data Lakehouse

- **Objetivo:** Conectar à API Pokémon e ingeri-los em um Data Lakehouse utilizando Databricks.
- **Tecnologias:** Python, Requests, Databricks.

### 2. Armazenamento em Formato Delta

- **Objetivo:** Armazenar os dados adquiridos no formato Delta para processamento eficiente e operações ACID.
- **Tecnologia:** Delta Lake, Databricks.

### 3. Criação de Tabelas para Análise

- **Objetivo:** Criar tabelas no Data Lakehouse para análise e relatórios de negócios.
- **Tecnologia:** SQL, Delta Lake, Databricks.

### 4. Integração de Código Spark, Python e SQL

- **Objetivo:** Mostrar como combinar Spark para processamento de dados, Python para automação e SQL para consultas.
- **Tecnologias:** PySpark, Python, SQL, Databricks.

### 5. Utilização de Multithreading

- **Objetivo:** Melhorar a eficiência da ingestão de dados usando multithreading para processamento paralelo.
- **Tecnologia:** Python `concurrent.futures`.

### 6. Monitoramento com `tqdm`

- **Objetivo:** Utilizar a biblioteca `tqdm` para exibir uma barra de progresso durante a execução do processo.
- **Tecnologia:** Python `tqdm`.

## Notas

- **Comentários:** O código fonte está bem comentado para facilitar o entendimento e a manutenção.
- **Tecnologias Utilizadas:** Python, Spark, Delta Lake, Databricks, Requests, `tqdm`.

Este README fornece uma visão geral do projeto e seus componentes principais. Para detalhes específicos do código e da implementação, consulte os arquivos de código-fonte correspondentes.

