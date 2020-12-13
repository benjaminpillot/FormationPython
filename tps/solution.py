# Lire un nombre entier entré par l'utilisateur
some_integer = int(input("Entrer un nombre entier positif et supérieur à 1:\n"))

# Initialiser une liste des possibles diviseurs
list_of_dividers = []

# Boucler sur l'ensemble des nombres entiers
# compris entre 2 et le nombre // 2 (la division
# entière est réalisée à l'aide de l'opérateur '//')
# Tester si le reste de la division entière est nul
# ou non à l'aide de l'opérateur modulo '%'. Si le
# reste est nul, on ajoute le nombre à la liste des
# diviseurs
for n in range(2, some_integer//2 + 1):
    if some_integer % n == 0:
        list_of_dividers.append(n)

# Si la liste est vide, le nombre est premier. Sinon,
# on affiche l'ensemble des diviseurs
if len(list_of_dividers) == 0:
    print(f"Le nombre {some_integer} est premier.")
else:
    print(f"Le nombre {some_integer} n'est pas premier. Il est divisible par : ", end='')
    print(*list_of_dividers, sep=", ")