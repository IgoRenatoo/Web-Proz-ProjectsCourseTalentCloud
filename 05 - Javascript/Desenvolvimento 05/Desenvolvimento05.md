# 📜 Desenvolvimento 01 

## 🎯 Descrição do Projeto 

Crie um projeto com dois arquivos: index.html e script.js. 

No arquivo 'index' insira a estrutura base HTML e dentro da tag 'body' inclua quatro tags vazias: h1, ul, a, ol. Adicione o atributo id="titulo" à tag h1, o atributo href="https://prozeducacao.com.br" à tag 'a', e o atributo id="lista-ordenada" à tag 'ol'. 

Na sequência, realize a conexão entre o arquivo HTML e o arquivo JavaScript.

No arquivo script.js capture os quatro elementos criados, e use a propriedade .innerText para adicionar conteúdo textual aos elementos 'h1' e 'a', e a propriedade .innerHTML para adicionar três itens simples na lista não ordenada, e três itens com links para outros sites na lista ordenada.  

## 🛠️ Resolução

```
=== HTML ===
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Desenvolvimento 05</title>    
</head>
<body>
    <h1 id="title">Teste!</h1>
    <ul></ul>
    <a href="https://prozeducacao.com.br"></a>
    <ol id="ordered-list"></ol>
</body>
<script src="main.js"></script>
</html>

=== JAVASCRIPT ===
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
