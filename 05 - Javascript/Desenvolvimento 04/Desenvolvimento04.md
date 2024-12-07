# 📜 Desenvolvimento 04

## 🎯 Descrição do Projeto 

Crie um novo projeto com dois arquivos: index.html e script.js. 

No arquivo HTML, defina a estrutura padrão HTML, e inclua uma tag h1 com o título "Conexão com um arquivo JavaScript". 

No arquivo JavaScript defina uma função que imprima a mensagem "Conexão feita com sucesso!" no terminal, e execute ela três vezes. 

Finalmente, conecte ambos arquivos, abra seu projeto no navegador usando a extensão LiveServer e confira se a mensagem foi impressa três vezes no terminal. 

## 🛠️ Resolução

```
=== HTML ===
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Conexão com um arquivo JavaScript</h1>
  <script src="main.js"></script>
</body>
</html>

=== JAVASCRIPT ===
function connectToServer () {
  console.log('Conexão feita com sucesso!')
}

connectToServer()
connectToServer()
connectToServer()


