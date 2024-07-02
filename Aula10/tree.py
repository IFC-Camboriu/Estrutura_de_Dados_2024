# Cria árvore binária com raiz r
def binary_tree(r):
    return [r, [], []]

# Insere novo ramo a esquerda da raiz
def insert_left(root, new_branch):
    # Analisa a subárvore a esquerda
    t = root.pop(1)
    # Se a subárvore a esquerda não é vazia
    if len(t) > 1:
        # Insere na posição 1 da raiz (esquerda)
        # Novo ramo será a raiz da subárvore a esquerda
    # Adiciona t na esquerda do novo ramo
        root.insert(1, [new_branch, t, []])
    else:
    # Se t for vazia, não há subárvore a esquerda
        root.insert(1, [new_branch, [], []])
    return root

# Insere novo ramo a direita da raiz
def insert_right(root, new_branch):
    # Analisa a subárvore a direita
    t = root.pop(2)
    # Se a subárvore a direita não é vazia
    if len(t) > 1:
    # Insere na posição 2 da raiz (direita)
    # Novo ramo será a raiz da subárvore a direita
    # Adiciona t na direita do novo ramo
        root.insert(2, [t, new_branch, [], ])
    else:
    # Se t for vazia, não há subárvore a direita
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]

# Cria árvore binária
r = binary_tree(3)
print(r)

# Adiciona subárvore a esquerda
insert_left(r, 4)
print(r)

# Adiciona subárvore a direita
insert_right(r, 7)
print(r)


print(get_right_child(r))
print(get_left_child(r))

print(get_root_val(r))

set_root_val(r, 23)

print(r)