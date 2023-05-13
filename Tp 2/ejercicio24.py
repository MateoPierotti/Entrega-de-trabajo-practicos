from pila import Pila


# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
class cualidades:
    def __init__(self, nombre, pelis):
        self.nombre = nombre
        self.pelis = pelis


stack = Pila()
aux = Pila()
letras = Pila()


def pila_marvel():
    stack.push(cualidades("Scarlet Witch", 3))
    stack.push(cualidades("Rocket Raccoon", 5))
    stack.push(cualidades("Iron Man", 8))
    stack.push(cualidades("Capitán América", 4))
    stack.push(cualidades("Thor", 7))
    stack.push(cualidades("Hulk", 3))
    stack.push(cualidades("Black Widow", 7))
    stack.push(cualidades("Hawkeye", 4))
    stack.push(cualidades("Spider-Man", 2))
    stack.push(cualidades("Doctor Strange", 2))
    stack.push(cualidades("Black Panther", 2))
    stack.push(cualidades("Ant-Man", 2))
    stack.push(cualidades("Vision", 2))

    stack.push(cualidades("Groot", 5))
    stack.push(cualidades("Falcon", 3))
    stack.push(cualidades("War Machine", 4))
    stack.push(cualidades("Winter Soldier", 3))

    stack.push(cualidades("Thanos", 3))
    stack.push(cualidades("Loki", 6))


pila_marvel()
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila


def posicion_groot_rocket(stack, aux):
    groot = 0
    rocket = 0
    for i in range(stack.size()):
        if stack.on_top().nombre == "Groot":
            groot = i + 1
            print(f'Groot se encuentra en la posicion {groot}')
            cosa = stack.pop()
            aux.push(cosa)
        elif stack.on_top().nombre == "Rocket Raccoon":
            rocket = i + 1
            print(f'Rocket se encuentra en la posicion {rocket}')
            cosa = stack.pop()
            aux.push(cosa)

        else:
            cosa = stack.pop()
            aux.push(cosa)

    return groot, rocket


# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# # car la cantidad de películas en la que aparece
# print(aux.on_top().nombre)
def mayor_a_cinco(aux):
    while aux.size() > 0:
        if aux.on_top().pelis >= 5:
            print(
                f'{aux.on_top().nombre} participo en {aux.on_top().pelis} peliculas de marvel')
            cosa = aux.pop()
            stack.push(cosa)
        else:
            cosa = aux.pop()
            stack.push(cosa)

# c. determinar en cuantas películas participo la Viuda Negra(Black Widow)


def peliculas_viuda_negra(stack):
    for i in range(stack.size()):
        if stack.on_top().nombre == 'Black Widow':
            print(
                f'{stack.on_top().nombre} participo en {stack.on_top().pelis} peliculas de marvel')
            cosa = stack.pop()
            aux.push(cosa)

        else:
            cosa = stack.pop()
            aux.push(cosa)

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
def empieza_c_d_g(stack, iniciales):
    personajes = []
    for i in range(stack.size()):
            for j in iniciales:
                if stack.on_top().nombre.lower().startswith(j) == True:
                    personajes.append(stack.on_top().nombre)
            stack.pop()
    return personajes



print()
print('¡En que posicion puedo encontrar a groot y a rocket dentro de mi pila?')
print()
posicion_groot_rocket(stack, aux)
print()
print('Protagonistas y cantidad de peliculas en las que participo (mayores que 5):')
print()
mayor_a_cinco(aux)
print()
print('¿cuantas peliculas protagonizo la viuda negra?')
print()
peliculas_viuda_negra(stack)
print()
print('Que personajes empiezan con las letras C, D y G?')
print()
pila_marvel()
iniciales = ['c', 'd', 'g']

for i in empieza_c_d_g(stack, iniciales):

    print(f"{i} empieza {i[0]}")
