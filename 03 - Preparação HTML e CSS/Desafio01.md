
# 📜 Desafio 01 - Preparação para HTML e CSS

## 🎯 Descrição do Projeto 

Estamos modernizando nossa loja e precisamos de um novo sistema de controle de estoque. Geralmente anotamos todos os produtos que temos disponíveis, e quando um dos produtos acaba, substituímos ele por algum outro produto.

Ouvi dizer que vocês podem fazer um sistema para a gente que mostra a `lista com todos nossos produtos`, e nos deixa `alterar um produto por outro`.

Além disso, estamos pensando em ampliar nosso armazém, para ter mais espaço para mais produtos. Então, se puderem fazer com que o sistema nos `permita adicionar mais produtos` à lista, e qualquer outra coisa que acharem necessário, seria muito bom.

## ⏳ Pendências

- [ ] Adicionar ao Menu a opção para `Relatório de estoque` quantidade crescente.

- [ ] Adicionar ao Menu a opção para `Relatório de estoque` quantidade decrescente.

- [ ] Adicionar ao Menu a opção para `excluir o item` no estoque.

- [ ] Adicionar ao Menu a opção para `retirada de item` no estoque.

- [ ] Após retirada, verificar se existe algum `item zerado` e propor tirar ele da lista ou alterar.

- [ ] Após retirada, mensagem de alerta para `nível crítico` do item no estoque. ( abaixo de 5 solicitar reposição )


## 🛠️ Resolução

<pre>
produtos = ["Arroz", "Feijão", "Macarrão", "Óleo de cozinha", "Açúcar"]
quantidades = [10, 1, 8, 15, 30]

def menu():
  while True:
    print("\nEscolha a opção desejada: 1. Listar todos os produtos, 2. Alterar produto, 3. Adicionar novo produto, 4. Sair")

    opcao = input("Opção desejada: ")

    if (opcao == '1'):
      print("Listar todos os produtos selecionado.")
      print(f"Produtos no estoque: {produtos}.")
      print(f"Quantidade no estoque: {quantidades}.")
    elif (opcao == '2'):
      print("Alterar produto selecionado.\n")
      alterar_produto()
    elif (opcao == '3'):
      print("Adicionar novo produto selecionado.")
      adicionar_produto()
    elif (opcao == '4'):
      print("Logout...")
      break
    else:
      print("Código inválida. Tente novamente.")

def alterar_produto():
  while True:
    print("Escolha a opção desejada: 1. Escolher a partir da lista, 2. Alterar produtos menor quantidade, 3. Alterar produtos zerados, 4. Sair")

    opcao = input("Opção desejada: ")

    if (opcao == '1'):
        for i in range(0, len(produtos)):
          print(f"Código: {i+1} - Produto {produtos[i]}, quantidade {quantidades[i]}")        
        indice = int(input("Digite o código do produto que deseja alterar: "))
        novo_produto = input("Digite o nome do novo produto: ")
        qtd_novo_produto = int(input("Digite a quantidade disponível do novo produto: "))
        if indice <= len(produtos) and indice > 0:
          produtos[indice-1] = novo_produto;
          quantidades[indice-1] = qtd_novo_produto;
          print(f"\nOs novos produtos são: {produtos}"); 
    
    elif (opcao == '2'):
      select_item = 0
      quantidade_produto = 100
      for i in range(0, len(produtos)):
        if quantidades[i] < quantidade_produto:
          quantidade_produto = quantidades[i]
          select_item = i
      print(f"O produto alterado será o: {produtos[select_item]}");
      produtos[select_item] = input("Digite o nome do novo produto: ");
      quantidades[select_item] = int(input("Digite a quantidade disponível do novo produto: "));
      print(f"\nOs novos produtos são: {produtos}");
    
    elif (opcao == '3'):
      for i in range(0, len(produtos)):
        if quantidades[i] == 0:
          print(f"O produto alterado será o: {produtos[i]}");
          produtos[i] = input("Digite o nome do novo produto: ");
          quantidades[i] = int(input("Digite a quantidade disponível do novo produto: "));
        else:
          print("Não há produtos zerados no estoque!")

    elif (opcao == '4'):
      print("Retornando ao menu inicial...")
      menu()
      break
    else:
      print("Código inválida. Tente novamente.")

def adicionar_produto():
    novo_produto = input("Digite o nome do novo produto: ")
    qtd_novo_produto = int(input("Digite a quantidade disponível do novo produto: "))
    produtos.append(novo_produto)
    quantidades.append(qtd_novo_produto)
    print(f"\nProduto '{novo_produto}' com {qtd_novo_produto} unidades foi adicionado ao estoque.")
    print(f"Produtos no estoque: {produtos}")
    print(f"Quantidade no estoque: {quantidades}")

menu();
</pre>
