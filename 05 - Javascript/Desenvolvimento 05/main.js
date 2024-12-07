const title = document.getElementById('title')
const listNoOrdered = document.querySelector('ul')
const link = document.querySelector('a')
const listOrdered = document.getElementById('ordered-list')

// Adicionando conteúdo textual
title.innerText = 'Bem-vindo ao Projeto!'
link.innerText = 'Acesse Proz Educação'

// Adicionando itens às listas
listNoOrdered.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`

listOrdered.innerHTML = `
    <li><a href="https://google.com" target="_blank">Google</a></li>
    <li><a href="https://youtube.com" target="_blank">YouTube</a></li>
    <li><a href="https://linkedin.com" target="_blank">linkedIn</a></li>
`
