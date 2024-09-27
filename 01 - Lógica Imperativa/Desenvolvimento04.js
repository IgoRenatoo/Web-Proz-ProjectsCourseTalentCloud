import prompt from 'prompt-sync'

let name = prompt()('Informe seu Nome! ~> ')
let address = prompt()('Informe seu Endereço! ~> ')
let city = prompt()('Informe seu Cidade! ~> ')
let CPF = prompt()('Informe seu CPF! ~> ')
let RG = prompt()('Informe seu RG! ~> ')

let data = []

data.push(name, address, city, CPF, RG)

console.log(data)