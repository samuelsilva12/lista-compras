# criar lista de compras que adicione produto, remova produto e exiba a lista de produtos e sair do programa
lista = []
#função para adicionar produtos a lista
def add_item(produto_lista):
  produto = input("adicione o nome do item ao carrinho: ")
  produto_lista.append(produto)
#função para remover item da lista de compras
def remover_item(item):
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' foi removido!")
    else:
        print(f"Item '{item}' não encontrado na lista.")
#exibir a lista
def exibir_itens():
  for produtos in lista:
    print(f"{produtos}")

opcao = ''
while opcao != '0':
  print(("\n*** Menu ***\n1 - Adicionar item\n2 - Remover item\n3 - Exibir lista\n0 - Sair\n"))
  opcao = input("Escolha uma opção: ")
  if opcao == '1':
  #chamando funçoes
    print("** ADICIONAR ITEM A LISTA: ")
    add_item(lista)
    opcao = input("Escolha uma opção: ")
  elif opcao == '2':
  # func remover produtos
    print("REMOVER ITEM: ")
    produto = input("Digite o nome do produto: ")
    remover_item(produto)
    opcao = input("Escolha uma opção: ")
  elif opcao == '3':
  # func exibir lista
    print("Lista de Produtos: ")
    exibir_itens()
    opcao = input("Escolha uma opção: ")
  elif opcao == '0':
    print(" programa encerrado!")