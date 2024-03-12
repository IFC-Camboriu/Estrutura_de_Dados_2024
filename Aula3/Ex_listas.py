N = 5
# declarando uma lista
lista = []

def insere_lista(x):
#insere elementos na lista
    lista.append(x)

def remove_lista(x):
# ajustar a função para não gerar erro caso o valor fornecido não seja encontrado na estrutura, não pode utilizar try...
# del, remove ou pop tem diferença?
    if x in lista:
        lista.remove(x)
    else: 
        print("Elemento não está na lista!")


def tamanho_lista():
    print("Tamanho da lista: ",len(lista))

def insere_na_posicao(x, i):
#inserir na posição sem perder a informação, ou seja, adicionar o elemento
#insere na ultima posição caso a posição não esteja na estrutura 
    if i < len(lista) and len(lista) < N:
        lista.insert(i, x)
    else:
        if(len(lista) < N):
            lista.append(x)
        else: 
            print("Elemento não pode ser inserido não há posições disponíveis.")



def consulta_valor(x):
#mostrar o índice do elemento presente na lista
    if x in lista:
        print(f"O elemento {x}, está na lista, na posição {lista.index(x)}!")
    else:
        print(f"O elemento {x}, não está na lista")


i = 0
while i < N:
    insere_lista(int(input("Informe um valor para a lista:")))
    i += 1
    print(lista)
print("____________________________________________________")

# Fazer os testes abaixo
remove_lista(lista[2])

print(lista)

tamanho_lista()

insere_na_posicao(2, 3)
print(lista)

consulta_valor(1)

insere_na_posicao(10, 2)

print(lista)
