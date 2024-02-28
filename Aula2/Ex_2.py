import numpy as np

# tamanho do array
N = 5

#preenche a estrutura com zeros
vetor_1 = np.zeros(N)

#preenche o vetor com valores do tipo float
for i in range(N):
    vetor_1[i] = float(input(f'Informe um valor para vetor[{i}]: '))

lista = []
for i in range(N):
    if vetor_1[i] != 0:
        lista.append(vetor_1[i])

print(lista)

# transformar para array caso necessário 
# Transforma a lista em um array NumPy
array_numpy = np.array(lista)

# Imprime o array resultante
print("Lista original:", lista)
print("Array NumPy:", array_numpy)
print(type(array_numpy))