# 📜 Desenvolvimento 01 

## 🎯 Descrição do Projeto 

Acesse o site OneCompiler ([--- Link ---](https://onecompiler.com/javascript/432c952dd)) e crie uma função que recebe dois números como parâmetros e imprime quatro frases no terminal (a partir de template strings) demonstrando as quatro operações básicas aplicadas a ambos números. Exemplo:

4 + 5 = 9
4 - 5 = -1
4 x 5 = 20
4 / 5 = 0.8 

## 🛠️ Resolução

```
=== JAVASCRIPT ===
function exec(num1, num2) {
    console.log(`${num1} + ${num2} = ${num1 + num2}`);
    console.log(`${num1} - ${num2} = ${num1 - num2}`);
    console.log(`${num1} x ${num2} = ${num1 * num2}`);
    console.log(`${num1} / ${num2} = ${num1 / num2}`);
}

exec(4, 5);
```
