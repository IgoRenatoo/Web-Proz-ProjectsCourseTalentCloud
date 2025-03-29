# 📜 Desenvolvimento 03 - Introdução à Programação

## 🎯 Descrição do Projeto 

Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

- Escreva um código que imprima todos os números exceto o número 13.
- Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

> <b>Extra:</b> Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

## 🛠️ Resolução

<pre>
# Estrutura de repetição FOR
for i in range(1, 21):
    if i != 13:
        print(f"Estrutura FOR: {i}")
</pre>

<pre>
# Estrutura de repetição WHHILE
i = 1
while i < 21:
  if i != 13:
     print(f"Estrutura WHHILE: {i}")
  i+=1
</pre>

<pre>
# Estrutura de repetição FOR decrescente
for i in range(20, 0, -1):
    if i != 13:
        print(f"Estrutura FOR decrescente: {i}")
</pre>
