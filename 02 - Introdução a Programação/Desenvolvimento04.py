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
