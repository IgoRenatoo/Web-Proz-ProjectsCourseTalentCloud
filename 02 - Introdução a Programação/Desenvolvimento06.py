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
