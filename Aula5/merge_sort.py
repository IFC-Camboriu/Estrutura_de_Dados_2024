# Merge sort in Python

def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista

data = [2,4,8,1,5,7]
data = mergeSort(data)
print('Lista Ordenada:')
print(data)