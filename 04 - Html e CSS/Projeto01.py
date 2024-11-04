nome = input("Informe seu nome para cadastro!");

def coworking():

  print("\nBem vindo ao Coworking Meet - Tudo que você precisa em um só lugar!");

  while True:
    print("Atualmente temos 2 opções de espaços!\n")
    print(" 1. Coworking TechNature - Seu espaço de trabalho em meio à natureza")
    print(" 2. Coworking MyHome - Conforto e tranquilidade, sua segunda casa")
    print(" 3. Sair da aplicação")

    opcao = input("\nDigite '1' para Coworking TechNature, '2' para Coworking MyHome ou '3' para sair da aplicação: ")
    if (opcao == '1'):
      technature()
    elif (opcao == '2'):
      myhome()
    elif opcao == '3':
      print("Desconect!")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

def technature():
  print("chegou aqui também")
def myhome():
  print("chegou aqui também")

coworking()
