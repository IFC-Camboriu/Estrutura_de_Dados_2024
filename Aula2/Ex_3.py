import numpy as np

# tamanho do array
N = 5
i = 0

#preenche a estrutura com zeros
vetor_1 = np.zeros(N)

#preenche o vetor com valores do tipo float
while i < N:
    temp = float(input(f'Informe um valor para vetor[{i}]:'))
    j = 0
    flag = 0
    while (j < i):
        if(vetor_1[j] == temp):
            flag = 1
            j += 1
        else:
            j += 1
    if(flag == 0):
        vetor_1[i] = temp
        i += 1
    else:
        print(f" O número {temp} já está no vetor! Informe outro valor!")

print(vetor_1)