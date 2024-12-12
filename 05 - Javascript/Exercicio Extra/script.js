/* eslint-disable no-unused-vars */
const book = document.querySelector('#book')
const btnSub = document.querySelector('#btnSub')
const qtdValue = document.querySelector('#qtdValue')
const btnAdd = document.querySelector('#btnAdd')
const total = document.querySelector('#total')
// Number(parâmetro) transforma o valor contído dentro dele em Number, no caso, '11.66'.
// textContent seleciona o texto contido no parâmetro selecionado, book.
// split é um method / função nátiva JS para separar um texto em um array a partir de um parâmetro, ele dividiu 'Valor: R$ 11.66' em 1 array com 2 posições, dados = ['Valor: , 11.66] logo, dados[1] = 11.66
const valueItem = Number(book.textContent.split('R$ ')[1])
let valueTotal = 0


function subtract () {
  if (qtdValue.value === '1') { btnSub.classList.add('hidden') }
  qtdValue.value--
  valueTotal = (valueTotal - valueItem).toFixed(2)
  book.innerHTML = `Valor: R$ ${valueTotal}`
  qtdValue.innerHTML = qtdValue.value + ' itens'
  total.innerHTML = `R$ ${valueTotal}`
}

function add () {
  btnSub.classList.remove('hidden')
  qtdValue.value++
  valueTotal = (valueItem * qtdValue.value).toFixed(2)
  book.innerHTML = `Valor: R$ ${valueTotal}`
  qtdValue.innerHTML = qtdValue.value + ' itens'
  total.innerHTML = `R$ ${valueTotal}`
}
