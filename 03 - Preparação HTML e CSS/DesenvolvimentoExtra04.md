
# 📜 Desenvolvimento Extra 04 - Preparação para HTML e CSS

## 🎯 Descrição do Projeto 

A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

`lista_produtos` = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

> Como desafio, adicione dois novos produtos da sua escolha à lista. 


## 🛠️ Resolução

<pre>
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

</pre>
