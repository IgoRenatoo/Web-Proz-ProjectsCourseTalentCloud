import prompt from 'prompt-sync'

const name = prompt()('Informe seu Nome! ~> ')
const address = prompt()('Informe seu Endereço! ~> ')
const city = prompt()('Informe seu Cidade! ~> ')
const CPF = prompt()('Informe seu CPF! ~> ')
const RG = prompt()('Informe seu RG! ~> ')

const data = []

data.push(name, address, city, CPF, RG)

console.log(data)
