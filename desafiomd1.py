
from random import choice
lista_clientes = []
telefone_clientes = []

while True:
    cliente = input("Digite o nome do cliente: ")
    if cliente == 'fim':
        break
    telefone = int(input("Digite o telefone do cliente: "))
    
    lista_clientes.append(cliente) # Acrescenta um item na lista
    telefone_clientes.append(telefone)

nome_telefone = zip(lista_clientes, telefone_clientes) # União das duas listas

cliente_escolhido = choice(list(nome_telefone)) # Sorteia um item dentro da lista
print(f"O nome e o telefone do cliente sorteado: {cliente_escolhido}")