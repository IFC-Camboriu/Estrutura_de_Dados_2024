import numpy as np
# Cria uma matriz 5x5 preenchida com zeros
matriz = np.zeros((5, 5), dtype=int)

# Preenche a diagonal principal com 1
np.fill_diagonal(matriz, 1)

# Exibe a matriz resultante
print("Matriz Resultante:")
print(matriz)