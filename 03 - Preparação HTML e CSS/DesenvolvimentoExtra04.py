lista_produtos = [
    'máscaras faciais', 
    'batons', 
    'esmaltes', 
    'perfumes', 
    'loções', 
    'xampus', 
    'sabonetes', 
    'delineadores'
]
        
lista_produtos.remove('delineadores') # Removendo o produto 'delineadores'

for i in range((len(lista_produtos))):
    if lista_produtos[i] == 'batons':
        lista_produtos[i] = 'rímel'
    elif lista_produtos[i] == 'loções':
        lista_produtos[i] = 'cremes hidratantes'
    elif i+1 == len(lista_produtos):
        lista_produtos.append('cremes para o rosto')  # Adiciona um produto
        lista_produtos.append('óleos corporais')  # Adiciona outro produto
        print("Lista de produtos: ", lista_produtos) # Imprimi a lista de produtos
