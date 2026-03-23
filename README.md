# projetointegradorgrupo56
Projeto Integrador - Grupo 56 - Ciência de Dados - Etapa 1
# Tema do Projeto: Análise de dados de vendas de uma loja

## 1. Integrantes
- Ana Luiza
- Beatriz
- Luan
- Matheus
- Sabrina
  
## 2. Base de dados e Contextualização
**Contexto e Origem:** Utilizaremos o dataset "Store Sales Forecasting Dataset", dispolibilizado publicamente na plataforma Kaggle. Esta base contém registros históricos de transações comerciais, englobando detalhes de faturamento, categorias de produtos e datas de venda.

**Link:** https://www.kaggle.com/datasets/tanayatipre/store-sales-forecasting-dataset

**Objetivo da Análise:** Analisar dados de vendas de uma loja para identificar padrões de consumo, os produtos mais vendidos e o comportamento e evolução das vendas ao longo do tempo.

## 3. Planejamento do Processo de ETL
Nosso projeto utilizará a linguagem Python para realizar as seguintes etapas:

## Planejamento das Tarefas
- Escolha e análise da base de dados
- Implementação do processo de ETL (Extração, Transformação e Carga)
- Limpeza e transformação dos dados
- Armazenamento dos dados em banco de dados
- Criação de um dashboard interativo

## 4. Divisão de Tarefas e Cronograma
Para garantir uma organização ágil e transparente, centralizamos as responsabilidades e os prazos na tabela abaixo. Cada membro lidera uma frente, seguindo a ordem lógica do processo de ETL

| Prazo | Etapa do Projeto | Responsável | Tarefa Principal |
| :--- | :--- | :--- | :--- |
| **Semana&nbsp;1** | Planejamento | **Sabrina** | Organização do repositório no GitHub, documentação inicial e definição da base. |
| **Semana&nbsp;2** | Extração (Extract) | **Matheus** | Configuração inicial do ambiente de código e extração dos dados. |
| **Semana&nbsp;3** | Transformação (Transform) | **Beatriz** | Tratamento e transformação dos dados utilizando a biblioteca **Pandas**. |
| **Semana&nbsp;4** | Carga (Load) | **Luan** | Modelagem e armazenamento dos dados estruturados no Banco de Dados. |
| **Semana&nbsp;5** | Visualização | **Ana Luiza** | Desenvolvimento do dashboard interativo utilizando a biblioteca **Streamlit**. |

## 5. Ideia Inicial do Dashboard

O dashboard interativo deverá apresentar as seguintes visualizações e indicadores:

**Cards (Indicadores):** Faturamento total e Quantidade total de itens vendidos.

**Gráfico de barras:** Volume de vendas por categoria de produto.

**Gráfico de Pizza/Rosca:** Proporção de vendas por região.

**Gráfico de Linhas:** Evolução das vendas ao longo do tempo (análise temporal).

## 6. Transformações de Dados Planejadas

Utilizando a biblioteca **Pandas**, pretendemos realizar algumas transformações nos dados, como:

- Tratamento de valores ausentes
- Padronização de nomes de colunas
- Conversão de campos de data para formato adequado
- Agregação de dados para cálculo de métricas de vendas
- Organização das tabelas para armazenamento em banco de dados.
