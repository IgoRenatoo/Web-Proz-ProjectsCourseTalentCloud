# 📜 Desenvolvimento 04 - Introdução à Programação

## 🎯 Descrição do Projeto 

Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

## 🛠️ Resolução

<pre>
def calcular(num1, num2, operacao):
  if operacao == 1:
    print(f"Operação de soma, resultado de {num1} + {num2} é = {num1 + num2}")

  elif operacao == 2:
    print(f"Operação de subtração, resultado de {num1} - {num2} é = {num1 - num2}")

  elif operacao == 3:
    print(f"Operação de multiplicação, resultado de {num1} * {num2} é = {num1 * num2}")

  elif operacao == 4:
    if (num2 == 0):
      print("Não existe divisão por 0, informe um outro número como divisor.")
    else: print(f"Operação de divisão, resultado de {num1} / {num2} é = {num1 / num2}")

  elif operacao > 4 or operacao < 1:
    print("Número invalido!")


calcular(2, 0, 4) # Chama a função com os parâmetros setados. Return: "Não existe divisão por 0, informe um outro número como divisor."
</pre>
