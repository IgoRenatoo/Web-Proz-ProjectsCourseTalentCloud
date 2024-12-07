// Método simples: Usando innerHTML para adicionar o título
const titulo = document.createElement('h1')
titulo.id = 'titulo'
titulo.innerHTML = 'Xhoppe Online'
document.body.appendChild(titulo)

// Método complexo: Criando elementos e estruturando manualmente
const produto = document.createElement('div')

// Adiciona o nome do produto
const nome = document.createElement('h2')
nome.innerText = 'Produto: Cadeira Gamer'
produto.appendChild(nome)

// Adiciona a descrição do produto
const descricao = document.createElement('p')
descricao.innerText = 'Cadeira ergonômica de alta qualidade, ideal para longas horas de trabalho ou jogos.'
produto.appendChild(descricao)

// Adiciona o preço do produto
const preco = document.createElement('p')
preco.innerText = 'Preço: R$ 762,99'
produto.appendChild(preco)

// Adiciona uma imagem ao produto
const imagem = document.createElement('img')
imagem.src = 'https://images.unsplash.com/photo-1575318634028-6a0cfcb60c59?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' // Imagem de exemplo
imagem.alt = 'Imagem de uma cadeira gamer'
imagem.style.width = '300px'
produto.appendChild(imagem)

// Adiciona o produto ao corpo do documento
document.body.appendChild(produto)
