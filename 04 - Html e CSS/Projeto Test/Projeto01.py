
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
      MyHome()
    elif opcao == '3':
      print("Desconect!")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

def technature():
  nome = input("Informe seu nome para cadastro!");
  coworking = 'TechNature'
  input_room = [] 
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

    #Visualizar Reservas
    elif (opcao == '3'):
      print(f"As reservas de {nome}, no coworking {coworking}são: \n")
      for i in input_room:
        print(f"{i} ✅")
    
    #Cancelar reservas
    elif (opcao == '4'):
      contador = 1
      print("Atualmente suas reservas são: \n")
      for i in input_room:
        print(f"{contador}. {i}")
        contador += 1
      cancelamento = int(input("\nQual deseja cancelar?"))
      for i in room:
        if (i.nome == input_room[cancelamento-1]):
          del input_room[cancelamento-1]
          i.disponivel = True

    #Voltar ao Menu Coworking Meet      
    elif (opcao == '5'):
      break
    
    #Tratamento de Error
    else:
      print("\nOpção inválida. Tente novamente.")

#  ----------------------------------------------------------------------------------------------  #

class CoworkingMyHome:
  pacote_basico = ['Mesa', 'Cadeira', 'Internet']
  pacote_medio = ['Sala de Reunião', 'Computador', 'Ar Condicionado', 'Impressora']
  pacote_avancado = ['Sala de Descanso', 'Projetor', 'Notebook', 'Espaço de lazer']
  pacote_premium = [pacote_basico, pacote_medio, pacote_avancado]

  def __init__(self):
    self.reservas = []
  
  def registrar_reserva(self, nome, data, hora, pacote):
    reserva = {"nome": nome, "data": data, "hora": hora, "pacote": pacote}
    self.reservas.append(reserva)
    print(f"Reserva registrada: {reserva}")

  def visualizar_reservas(self):
    if not self.reservas:
      print("Nenhuma reserva encontrada.")
    else:
      for reserva in self.reservas:
        print(reserva)

  def consultar_disponibilidade(self, data, hora, pacote):
    for reserva in self.reservas:
      if reserva["data"] == data and reserva["hora"] == hora and reserva["pacote"] == pacote:
        print(f"Indisponível: {reserva}")
        return False
    print("Disponível")
    return True

def MyHome():
  sistema = CoworkingMyHome()
  while True:
    print('\n1. Registrar Reserva')
    print('2. Visualizar Reservas')
    print('3. Consultar Disponibilidade')
    print('4. Voltar ao Coworking Meet')
      
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
      nome = input('Nome: ')
      data = input('Data (dd/mm/aaaa): ')
      hora = input('Hora (hh:mm): ')
      pacote = input('Pacote (basico, medio, avancado ou premium): ')
      sistema.registrar_reserva(nome, data, hora, pacote)

    elif escolha == '2':
      sistema.visualizar_reservas()

    elif escolha == '3':
      data = input('Data (dd/mm/aaaa): ')
      hora = input('Hora (hh:mm): ')
      pacote = input('Pacote (basico, medio, avancado ou premium): ')
      sistema.consultar_disponibilidade(data, hora, pacote)

    elif escolha == '4':
      print("Saindo do sistema.")
      break
    else:
      print("Opção inválida. Tente novamente.")

coworking()
