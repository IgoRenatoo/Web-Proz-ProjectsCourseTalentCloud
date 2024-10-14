# 📜 Desenvolvimento 06 - Introdução à Programação

## 🎯 Descrição do Projeto 

Desenvolva um programa que recebe do usuário `nome completo`, `ano atual` e `ano de nascimento` que seja entre <b>1922</b> e <b>2024</b>.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

## 🛠️ Resolução

<pre>
nome = input("Digite seu nome completo: ")
current_year = int(input("Informe o ano atual! "))
birthday_year = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))

def age_calculator(nome, current_year, birthday_year):
    if birthday_year < 1922 or birthday_year > current_year:
      print(f"{nome}, você digitou um ano inválido!")
    else:
      age = current_year - birthday_year    
      print(f"{nome}, você completou ou completará {age} anos em 2022.")

age_calculator(nome, current_year, birthday_year)
</pre>
