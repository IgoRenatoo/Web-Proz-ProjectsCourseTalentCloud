# 📜 Desenvolvimento 01 

## 🎯 Descrição do Projeto 

O Sistema de Gerenciamento de Bancos de Dados é um conjunto de programas que serve para gerenciar um ou mais bancos de dados. Sendo assim, pesquise sobre os bancos de dados mais utilizados no mercado de trabalho e descreva dois deles.

## 🛠️ Resolução

### 📌 Banco de Dados SQL (Relacional)
- 🔹 **Modelo Estruturado:** Dados armazenados em tabelas com colunas e linhas, seguindo um esquema rígido.  
- 🔹 **Linguagem SQL:** Utiliza **SQL (Structured Query Language)** para manipulação e consulta de dados.  
- 🔹 **Relacionamentos:** Suporta **joins** e normalização para evitar redundância.  
- 🔹 **Transações ACID:** Garante **Atomicidade, Consistência, Isolamento e Durabilidade**.  
- 🔹 **Escalabilidade Vertical:** Expansão ocorre aumentando os recursos do servidor.  
- 🔹 **Exemplos:** MySQL, PostgreSQL, SQL Server, Oracle, MariaDB.  

### 📌 Banco de Dados NoSQL (Não Relacional)
- 🔹 **Modelo Flexível:** Não exige esquema fixo, permitindo estruturas variadas de dados.  
- 🔹 **Tipos de Armazenamento:** Pode ser baseado em **documentos, chave-valor, colunas ou grafos**.  
- 🔹 **Alto Desempenho:** Otimizado para **grandes volumes de dados** e operações rápidas.  
- 🔹 **Escalabilidade Horizontal:** Expansão ocorre distribuindo os dados entre vários servidores.  
- 🔹 **Eventual Consistency:** Pode sacrificar consistência imediata para aumentar a disponibilidade.  
- 🔹 **Exemplos:** MongoDB (documentos), Redis (chave-valor), Cassandra (colunar), Neo4j (grafos).  

### 📊 Diferenças Principais

| Característica  | SQL (Relacional) | NoSQL (Não Relacional) |
|---------------|----------------|------------------|
| **Modelo de Dados** | Estruturado (Tabelas) | Flexível (Documentos, Chave-Valor, Grafos, Colunar) |
| **Linguagem** | SQL | Varia (JSON, BSON, APIs) |
| **Relacionamentos** | Suporta Joins | Relacionamentos menos comuns |
| **Transações** | ACID (Consistência Firme) | Eventual Consistency |
| **Escalabilidade** | Vertical (aumenta poder do servidor) | Horizontal (mais servidores) |
| **Casos de Uso** | ERPs, CRMs, Financeiro | Big Data, Streaming, IoT |

### 🎯 Quando Usar Cada Um?
- **Use SQL** quando precisar de **transações seguras**, **relacionamentos complexos** e **dados bem estruturados**.  
- **Use NoSQL** para **grandes volumes de dados**, **escalabilidade horizontal** e **flexibilidade no armazenamento**.  

