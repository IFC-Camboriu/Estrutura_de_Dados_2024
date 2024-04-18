# Bubble sort in Python

def bubbleSort(lista):
    
  # loop para acessar cada elemento da lista
  for i in range(len(lista)- 1):
    print(lista)
 # loop para comparar os elementos
    for j in range(0, len(lista) - i - 1):

      # compare de dois em dois elementos
      # modificar > para < para ordenar de forma decrescente
      if lista[j] > lista[j + 1]:
        # troca dos elementos
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Lista Ordenada:')
print(data)