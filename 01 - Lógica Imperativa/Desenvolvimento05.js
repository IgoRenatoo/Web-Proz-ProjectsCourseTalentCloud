import prompt from 'prompt-sync'

const fumaOuAnimal = prompt()('Você é fumante ou está com um animal de estimação? (sim/não): ').toLowerCase()
const group = parseInt(prompt()('Quantas pessoas estão no grupo? '))

if (fumaOuAnimal === 'sim') {
  console.log('Você será alocado na área externa.')
} else if (group >= 5) {
  console.log('Você será alocado no 1º andar.')
} else {
  console.log('Você será alocado no térreo.')
}