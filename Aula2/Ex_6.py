import numpy as np

# define o tamanho do array
N = 3
#preenche a estrutura com zeros
matriz = np.zeros((N,N))
vetor = np.zeros(N)

#mostra a matriz
print(matriz)


# Preenche a matriz conforme as condições dadas
for i in range(N):
    for j in range(N):
        matriz[i][j] = int(input(f'Informe um valor para Matriz[{i}][{j}]: '))

for l in range(N):
    for c in range(N):
        vetor[c] += matriz[l][c]

print(vetor)