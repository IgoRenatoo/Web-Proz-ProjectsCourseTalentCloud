# 📜 Desenvolvimento 02 - Introdução à Programação

## 🎯 Descrição do Projeto 

Desenvolva um algoritmo que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

## 🛠️ Resolução

<pre>
def category(rodas, peso_bruto, pessoas):
  if rodas == 2 or rodas == 3:
    return "Categoria A: Veículos com duas ou três rodas."
  elif rodas == 4:
    if pessoas <= 8 and peso_bruto <= 3500:
      return "Categoria B: Veículos com quatro rodas, que acomodam até oito pessoas e peso até 3500 kg."
    elif peso_bruto > 3500 and peso_bruto <= 6000:
      return "Categoria C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg."
    elif pessoas > 8:
      return "Categoria D: Veículos com quatro rodas ou mais que acomodam mais de oito pessoas."
  elif rodas >= 4:
    if peso_bruto > 6000:
      return "Categoria E: Veículos com quatro rodas ou mais e com mais de 6000 kg."

  return "Dados inválidos ou veículo não se enquadra em nenhuma categoria."

""" Uso """
rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso bruto em kg do veículo: "))
pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

print(category)
</pre>
