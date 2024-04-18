# Quick sort in Python

def quickSort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quickSort(a, ini, pp)
        quickSort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    # para uma versão com partição aleatória
    # descomente as próximas três linhas:
    # from random import randrange
    # rand = randrange(ini, fim)
    # a[rand], a[fim - 1] = a[fim - 1], a[rand]
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1

data = [-2, 45, 0, 11, -9]
data = quickSort(data)
print('Lista Ordenada:')
print(data)
