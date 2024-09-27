import prompt from 'prompt-sync'

const nomeEquipe = prompt()('Informe o nome da equipe: ');

for (let i = 1; i <= 5; i++) {
    console.log(`${nomeEquipe} - ${i}`);
}