nome = input("Informe seu nome para cadastro!");
coworking = 'not_found'
input_room = []

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
  coworking = 'TechNature'
  class Room:
    def __init__(self, nome, disponivel):
      self.nome = nome
      self.disponivel = disponivel
  room = [
    Room("Savana", True),
    Room("Gatolandia", True),
    Room("Cachorrolandia", True),
    Room("Passarolandia", True),
    Room("Verde e paz", True)
  ]
  room[1].disponivel = False;

  print("\nBem vindo ao TechNature - Seu espaço de trabalho em meio à natureza!");
  while True:
    print("\n*** Menu de Navegação ***");
    print("\nSelecione a opção desejada");
    print(" 1. Visualizar disponibilidade")
    print(" 2. Registrar Reservas")
    print(" 3. Visualizar Reservas")
    print(" 4. Cancelar reserva") # Feature Extra!
    print(" 5. Voltar ao Coworking Meet")

    opcao = input("\nOpção desejada: ")

    # Visualizar Disponibilidade
    if (opcao == '1'):
      print("Disponibilidade das nossas salas: \n")
      for i in room:
        if i.disponivel:
          print(f"{i.nome} está disponível. ✅")
        else:
          print(f"{i.nome} está indisponível. ❌")

    #Registrar Reservas
    elif (opcao == '2'):
      if all(not i.disponivel for i in room):
        print("\nAtenção! Atualmente não temos salas disponíveis!")
        continue 

      print("\nEssas são as salas disponíveis para reservas: ")
      contador = 1
      for i in room:
        if i.disponivel:
          print(f"{contador}. {i.nome} está disponível. ✅")
          contador += 1
        else:
          contador += 1        

      reserva = int(input("\nQual sala você deseja reservar: "))       

      if ( room[reserva-1].disponivel ):
        room[reserva-1].disponivel = False;
        print(f"Reserva na {room[reserva-1].nome} realizada com sucesso!")
        input_room.append(room[reserva-1].nome)
      else:
        print("\nAtenção! Número digitado não está disponível para reservas!")

def myhome():
  print("chegou aqui também")

coworking()
