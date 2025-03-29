# 📜 Desenvolvimento 05

## 🎯 Descrição do Projeto 

Elabore um algoritmo que possa descobrir, através de perguntas e respostas, em qual área de um restaurante uma pessoa ou grupo de pessoas precisa ser alocada.

O restaurante tem três áreas: térreo, 1ro andar, e área externa.

- Clientes fumantes ou com animais de estimação precisam ser alocadas na área externa.
- Grupos de 5 ou mais precisam ser alocados no 1º andar, pois não dá para juntar mesas no térreo.
- Qualquer outro grupo de pessoas pode ser alocado no térreo. 


## ⚙️ Tecnologias Utilizadas

- Javascript
- NodeJs
- Biblioteca `prompt-sync`

## 🧩 Instrução de uso

- Instale o NodeJS na sua máquina.
- Faça o fork do projeto em `https://github.com/IgoRenatoo/Proz-ProjectsCourseTalentCloud.git`.
- Utilize o comando `npm run dev05` para rodar o projeto.

## 🛠️ Resolução

<pre>import prompt from 'prompt-sync'

const fumaOuAnimal = prompt()('Você é fumante ou está com um animal de estimação? (sim/não): ').toLowerCase();
const group = parseInt(prompt()('Quantas pessoas estão no grupo? '));

if (fumaOuAnimal === 'sim') {
    console.log('Você será alocado na área externa.');
} else if (group >= 5) {
    console.log('Você será alocado no 1º andar.');
} else {
    console.log('Você será alocado no térreo.');
}</pre>