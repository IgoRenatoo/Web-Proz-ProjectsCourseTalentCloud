# 📜 Desenvolvimento 04

## 🎯 Descrição do Projeto 

Elabore um algoritmo para que o usuário, através da entrada de dados, informe os seus dados pessoais. Alguns desses dados
fornecidos pelo usuário precisam ser apresentados na tela quando o algoritmo for executado, são eles:
 
- Nome;
- Endereço;
- Cidade;
- CPF;
- RG.

## ⚙️ Tecnologias Utilizadas

- Javascript
- NodeJs
- Biblioteca `prompt-sync`

## 🧩 Instrução de uso

- Instale o NodeJS na sua máquina.
- Faça o fork do projeto em `https://github.com/IgoRenatoo/Proz-ProjectsCourseTalentCloud.git`.
- Utilize o comando `npm run dev04` para rodar o projeto.

## 🛠️ Resolução

<pre>import prompt from 'prompt-sync'

let name = prompt()('Informe seu Nome! ~> ')
let address = prompt()('Informe seu Endereço! ~> ')
let city = prompt()('Informe seu Cidade! ~> ')
let CPF = prompt()('Informe seu CPF! ~> ')
let RG = prompt()('Informe seu RG! ~> ')

let data = []

data.push(name, address, city, CPF, RG)

console.log(data)</pre>