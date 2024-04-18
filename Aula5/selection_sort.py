# Selection sort in Python


def selectionSort(lista, size):
   
    for step in range(size):
        min_idx = step
        print(lista) 
        for i in range(step + 1, size):
         
            # para ordenar descrescente, mudar > para < na linha 13
            # seleciona o menor número a cada loop
            if lista[i] < lista[min_idx]:
                min_idx = i
         
        # coloca o menor valor na posição correta
        (lista[step], lista[min_idx]) = (lista[min_idx], lista[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Lista Ordenada:')
print(data)