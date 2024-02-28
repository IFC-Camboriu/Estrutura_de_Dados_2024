import numpy as np

# tamanho do array
N = 5

#preenche a estrutura com zeros
vetor_1 = np.zeros(N)
vetor_2 = np.zeros(N)

#preenche o vetor com valores do tipo float
for i in range(N):
    vetor_1[i] = float(input(f'Informe um valor para vetor[{i}]: '))

#preenche o vetor com valores do tipo float
for i in range(N):
    vetor_2[i] = float(input(f'Informe um valor para vetor[{i}]: '))

print(type(vetor_1))
print(vetor_1)
print(vetor_2)

produto = 0
for i in range(N):
   produto += vetor_1[i] * vetor_2[i]

print(f"O produto escalar é: {produto}")