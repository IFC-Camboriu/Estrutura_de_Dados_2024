# Insertion sort in Python


def insertionSort(lista):

    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1
        # Compare a chave key com cada elemento da esquerda até  o menor elemento ser encontrado
        # Para ordenação decrescente, mudar key < lista[j] para  key > lista[j]. 
        print(lista)       
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        
        # coloca a chave após o elemnto menor que a chave(key).
        lista[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Lista Ordenada:')
print(data)