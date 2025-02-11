# 📜 Desenvolvimento 02

## 🎯 Descrição do Projeto 

O desenvolvimento de um projeto de banco de dados passa por fases importantes para a sua implementação, como a de projeto conceitual. Diante disso, crie uma entidade que tenha atributos simples, composto e multivalorado.

## 🛠️ Resolução

### Entidade: Pessoa

#### 📌 Atributos:
- **CPF** (*Simples*): `123.456.789-00`  
- **Nome Completo** (*Composto*): `{Primeiro Nome: João, Sobrenome: Silva}`  
- **Endereço** (*Composto*): `{Rua: Av. Brasil, Número: 100, Cidade: São Paulo, Estado: SP, CEP: 01000-000}`  
- **Telefones** (*Multivalorado*): `["(11) 99999-9999", "(11) 98888-8888"]`  
- **E-mails** (*Multivalorado*): `["joao@email.com", "joaosilva@trabalho.com"]`  
- **Data de Nascimento** (*Simples*): `15/08/1990`  

### 🛠 Explicação:
- **Atributos Simples** são indivisíveis, como `CPF` e `Data de Nascimento`.  
- **Atributos Compostos** podem ser divididos em partes menores, como `Nome Completo` e `Endereço`.  
- **Atributos Multivalorados** podem ter múltiplos valores, como `Telefones` e `E-mails`.  
