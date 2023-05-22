from cola import Cola
from pila import Pila

# Se tienen una cola con personajes de Marvel Cinematic Universe(MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género(Masculino M y Femenino F)
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro -
#                                                                                                                                                  manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel
# b. mostrar los nombre de los superhéroes femeninos
# c. mostrar los nombres de los personajes masculinos
# d. determinar el nombre del superhéroe del personaje Scott Lang
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
cola = Cola()


class caracteristicas:
    def __init__(self, nombre_personaje, nombre_heroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_heroe = nombre_heroe
        self.genero = genero


def marvel():
    cola.arrive(caracteristicas("Tony Stark", "Iron Man", "M"))
    cola.arrive(caracteristicas("Steve Rogers", "Capitán América", "M"))
    cola.arrive(caracteristicas("Natasha Romanoff", "Black Widow", "F"))
    cola.arrive(caracteristicas("Carol Danvers", "Capitana Marvel", "F"))
    cola.arrive(caracteristicas("Scott Lang", "Ant Man", "M"))
    cola.arrive(caracteristicas("Peter Parker", "Spider Man", "M"))


# muestra el nombre y la posicion(no pedida) de capitana
def capitana(cola):
    cont = 0
    while cola.size() > 0:
        if cola.on_front().nombre_heroe == "Capitana Marvel":
            cont += 1

            print(f"El nombre de Capitana Marvel es {cola.on_front().nombre_personaje}")
            print()
            print(f"se encuentra en la posicion {cont} de la cola")
            print()
            cola.atention()
        else:
            cola.atention()
            cont += 1
    return cont


# muestra personajes femeninos
def pers_femeninos(cola):
    while cola.size() > 0:
        if cola.on_front().genero == "F":
            print(cola.on_front().nombre_heroe)
            print()
            cola.atention()
        else:
            cola.atention()


# muestra personajes masculinos
def pers_masculinos(cola):
    while cola.size() > 0:
        if cola.on_front().genero == "M":
            print(cola.on_front().nombre_heroe)
            print()
            cola.atention()
        else:
            cola.atention()


# muestra el nombre y la posicion(no pedida) de capitana


def ant_man(cola):
    cont = 0
    while cola.size() > 0:
        if cola.on_front().nombre_personaje == "Scott Lang":
            cont += 1

            print(f"El nombre de heroe de Scott Lang es {cola.on_front().nombre_heroe}")
            print()
            print(f"se encuentra en la posicion {cont} de la cola")
            print()
            cola.atention()
        else:
            cola.atention()
            cont += 1
    return cont


# muestra el nombre de heroe de Carol Danvers y su posicion en la cola
def Carol_Danvers(cola):
    cont = 0
    while cola.size() > 0:
        if cola.on_front().nombre_personaje == "Carol Danvers":
            cont += 1

            print(
                f"El nombre de super heroe de Carol Danvers es {cola.on_front().nombre_heroe}"
            )
            print()
            print(f"se encuentra en la posicion {cont} de la cola")
            print()
            cola.atention()
        else:
            cola.atention()
            cont += 1
    return cont


# mostrar la primera letra
def primera_letra_s(cola):
    while cola.size() > 0:
        if cola.on_front().nombre_heroe[0] == "S":
            print(f"Heroes que arrancacon la letra S {cola.on_front().nombre_heroe}")
            print()
            cola.atention()

        elif cola.on_front().nombre_personaje[0] == "S":
            print(
                f"Personajes que arranca con la letra S {cola.on_front().nombre_personaje}"
            )
            print()
            cola.atention()

        else:
            cola.atention()


marvel()
print()
print("--------------------------------------------------------------------")
capitana(cola)

print("--------------------------------------------------------------------")

print("_Super heroes Femeninos_")
print()
marvel()
pers_femeninos(cola)

print("--------------------------------------------------------------------")

print("_Super heroes Masculinos_")
print()
marvel()
pers_masculinos(cola)

print("--------------------------------------------------------------------")

marvel()
ant_man(cola)

print("--------------------------------------------------------------------")

marvel()
Carol_Danvers(cola)

print("--------------------------------------------------------------------")

print('_Personaje o heroe que su primera letra es "S"_')


marvel()
print()
primera_letra_s(cola)
