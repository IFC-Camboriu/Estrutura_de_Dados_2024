# tamanho do conjunto
N = 5

vetor_1 = set()
vetor_2 = set()

for i in range(N):
    vetor_1.add(float(input(f"Informe valores para vetor_1 [{i}]")))

for i in range(N):
    vetor_2.add(float(input(f"Informe valores para vetor_1 [{i}]")))

print(type(vetor_1))
print(vetor_1)
print(vetor_2)

produto = 0
for i in range(N):
   produto += vetor_1[i] * vetor_2[i]

print(f"O produto escalar é: {produto}")