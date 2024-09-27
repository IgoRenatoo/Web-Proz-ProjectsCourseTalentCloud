# 📜 Desenvolvimento 05

## 🎯 Descrição do Projeto 

Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os identifiquem. Por exemplo, se o nome da equipe é “Os Lutadores”, o primeiro membro deve ter uma etiqueta “Os Lutadores – 1", o segundo membro “Os Lutadores – 2", e assim pela frente.

- Elabore um algoritmo que permita ao usuário inserir o nome da equipe, e imprime etiquetas para os 5 membros da equipe seguindo o exemplo mostrado acima.


## ⚙️ Tecnologias Utilizadas

- Javascript
- Estrutura de repetição `for`
- NodeJs
- Biblioteca `prompt-sync`

## 🧩 Instrução de uso

- Instale o NodeJS na sua máquina.
- Faça o fork do projeto em `https://github.com/IgoRenatoo/Proz-ProjectsCourseTalentCloud.git`.
- Utilize o comando `npm run dev06` para rodar o projeto.

## 🛠️ Resolução

<pre>import prompt from 'prompt-sync'

const nomeEquipe = prompt()('Informe o nome da equipe: ');

for (let i = 1; i <= 5; i++) {
    console.log(`${nomeEquipe} - ${i}`);
}</pre>