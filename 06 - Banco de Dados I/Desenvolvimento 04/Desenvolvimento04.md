# 📜 Desenvolvimento 04

## 🎯 Descrição do Projeto 

De acordo com os conceitos estudados, exiba os resultados das consultas das operações select, project, união, intersecção e diferença. Siga as instruções com base na tabela apresentada em anexo.

- Mostre as informações apenas dos alunos aprovados. A aprovação é acima de 7,0;
- Exiba as informações dos alunos do primeiro ano com nota maior ou igual a 8,0;
- Exiba apenas os nomes e as notas dos alunos;
- Crie uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor;
- Crie uma tabela ALUNO com o primeiro e o último nome de cada;
- Mostre o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
- Exiba o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
- Exiba o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR. 

## 🛠️ Resolução

### 📌 Consultas Relacionais  

- **Selecionar alunos aprovados (Nota > 7.0):**
  ```sql
  SELECT * FROM ALUNO WHERE Nota > 7.0;

- **Selecionar alunos do primeiro ano com nota ≥ 8.0:**
  ```sql
  SELECT * FROM ALUNO WHERE Ano = '1º' AND Nota >= 8.0;

- **Exibir apenas nome e nota dos alunos:**
  ```sql
  SELECT PNome, Nota FROM ALUNO;

- **Criar a tabela PROFESSOR (Apenas primeiro e último nome):**
  ```sql
  SELECT PNome, UNome FROM PROFESSOR;

- **Criar a tabela ALUNO (Apenas primeiro e último nome):**
  ```sql
  SELECT PNome, UNome FROM ALUNO;

- **União entre ALUNO(PNome, UNome) e PROFESSOR(PNome, UNome):**
  ```sql
  SELECT PNome, UNome FROM ALUNO  
  UNION  
  SELECT PNome, UNome FROM PROFESSOR;

- **Interseção entre ALUNO(PNome, UNome) e PROFESSOR(PNome, UNome):**
  ```sql
  SELECT PNome, UNome FROM ALUNO  
  INTERSECT  
  SELECT PNome, UNome FROM PROFESSOR;

- **Diferença entre ALUNO(PNome, UNome) e PROFESSOR(PNome, UNome):**
  ```sql
  SELECT PNome, UNome FROM ALUNO  
  EXCEPT  
  SELECT PNome, UNome FROM PROFESSOR;
