def calcular():
  while True:
    print(f"Seleciona a operação, 1: Soma, 2: Substração, 3: Multiplicação, 4: Divisão ou 0: Sair")
    operacao = input("Digite aqui a operação desejada: ")

    if operacao not in ['1', '2', '3', '4', '0']:
      print(f"Digite outro número,o número {operacao} não é válido!.")
      continue

    if operacao == '0':
      print("Opção escolhida: Sair da aplicação!")
      break;
    
    try:
      num1 = int(input("Digite o 1ª número!"))
      num2 = int(input("Digite o 2ª número!"))
    except ValueError:
      print("Valor incorreto, os números devem ser != de 0")
      continue

    if operacao == '1':
      print(f"Operação de soma, resultado de {num1} + {num2} é = {num1 + num2}")
    elif operacao == '2':
      print(f"Operação de subtração, resultado de {num1} - {num2} é = {num1 - num2}")
    elif operacao == '3':
      print(f"Operação de multiplicação, resultado de {num1} * {num2} é = {num1 * num2}")
    elif operacao == '4':
      print(f"Operação de divisão, resultado de {num1} / {num2} é = {num1 / num2}")


calcular() # Chama a função.
