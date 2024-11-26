# 📜 Desenvolvimento 01

## 🎯 Descrição do Projeto

A cidade do Recife é uma das mais famosas do Nordeste, ela possui diversos pontos turísticos e um deles é o Marco Zero. Sabendo disso, crie uma página HTML, falando sobre esse ponto turístico de acordo com os seguintes pré-requisitos: 

 1. A página precisa ter cabeçalho, conteúdo e rodapé;
 2. A página precisa ter imagens; 
 3. Use a tag de semântica textual inline. 


## 🛠️ Resolução

```
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marco Zero - Recife</title>
    <link rel="stylesheet" href="./global.css">
</head>
<body>
    <header>
        <img src="../assets/Desenvolvimento03/banner.jpg" alt="Banner do Marco Zero">
        <h1>Bem-vindo ao Marco Zero de Recife</h1>
    </header>

    <main>
        <section>
            <h2>Sobre o Marco Zero</h2>
            <div class="content">
                <p class="text-marco">O <b style="color: blue;">Marco Zero</b> é um dos pontos turísticos mais icônicos de Recife. Localizado no centro histórico da cidade, ele marca o início das principais vias que levam aos diversos bairros da capital pernambucana.</p>
                <img src="../assets/Desenvolvimento03/marco-zero.jpg" alt="Imagem do Marco Zero">
            </div>
        </section>
        
        <section>
            <h2>O que fazer no Marco Zero?</h2>
            <div class="content">
                <img src="../assets/Desenvolvimento03/frevo.jpg" alt="Paço do Frevo">
                <p class="text-frevo">No entorno do Marco Zero, você pode encontrar várias atrações culturais, como o <b style="color: red;">Paço do Frevo</b>, exposições de arte e apresentações ao ar livre. Além disso, a vista para o Recife Antigo e o porto é simplesmente deslumbrante.</p>
            </div>
        </section>
    </main>

    <footer>
        <p>26/11/2024 - Exercício HTML / CSS</p>
    </footer>
</body>
</html>
```
