# 2. Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje(puede ser vacio),
# grupo al que(perteneces puede ser vacio), año de aparición, por
# ejemplo(Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
# Resolver las siguientes tareas:



# h. Cargue al menos 20 superheroes a la lista.

from lista import Lista
from cola import Cola
from pila import Pila

lista = Lista()
cola = Cola()
pila = Pila()
cola1 = Cola()
lista1 =Lista()
lista2 = Lista()
lista_1 = Lista()
class Personajes():
    def __init__(self, supername, name, team, year):
        self.supername = supername
        self.name = name
        self.team = team
        self.year = year

    def __str__(self):
        return f"Superame: {self.supername}, Name : {self.name}, Team : {self.team}, Year : {self.year}"


def superhéroes():
    
    lista.insert(Personajes('Star-Lord', 'Peter Quill','Guardianes de la Galaxia', 1976), 'supername')
    lista.insert(Personajes('Señor de las Estrellas','Peter Quill', 'Guardianes de la Galaxia', 1976), 'supername')
    lista.insert(Personajes('Drax el Destructor', 'Arthur Douglas','Guardianes de la Galaxia', 1973), 'supername')
    lista.insert(Personajes('Gamora', 'Gamora','Guardianes de la Galaxia', 1975), 'supername')
    lista.insert(Personajes('Groot', 'Groot','Guardianes de la Galaxia', 1960), 'supername')
    lista.insert(Personajes('Rocket Raccoon', 'Rocket','Guardianes de la Galaxia', 1976), 'supername')
    lista.insert(Personajes('Sr. Fantástico', 'Reed Richards','Los Cuatro Fantásticos', 1961), 'supername')
    lista.insert(Personajes('La Mujer Invisible', 'Susan Storm','Los Cuatro Fantásticos', 1961), 'supername')
    lista.insert(Personajes('La Antorcha Humana', 'Johnny Storm', 'Los Cuatro Fantásticos', 1961), 'supername')
    lista.insert(Personajes('La Cosa', 'Ben Grimm', 'Los Cuatro Fantásticos', 1961), 'supername')
    lista.insert(Personajes('Vlack Widow', 'Natasha Romanoff', 'Vengadores', 1964), 'supername')
    lista.insert(Personajes('Capitana Marvel', 'Carol Danvers', 'Vengadores', 1968), 'supername')
    lista.insert(Personajes('Iron Man', 'Tony Stark','Vengadores',  1963), 'supername')
    lista.insert(Personajes('Capitán América', 'Steve Rogers','Vengadores', 1941), 'supername')
    lista.insert(Personajes('Thor', 'Thor' , 'Vengadores' ,1962), 'supername')
    lista.insert(Personajes('Hulk', 'Bruce Banner','Vengadores', 1962), 'supername')
    lista.insert(Personajes('Hawkeye','Clint Barton', 'Vengadores',1964), 'supername')
    lista.insert(Personajes('Viuda Negra','Yelena Belova', 'Vengadores', 1999), 'supername')
    lista.insert(Personajes('Pantera Negra','T-Challa' , 'Vengadores',1966), 'supername')
    lista.insert(Personajes('Doctor Strange', 'Stephen Strange','Vengadores', 1963), 'supername')

# a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje


def capitana_marvel(lista):
    indice = lista.search_r('Capitana Marvel', 0, lista.size()-1, 'supername')
    if indice != None:
        value = lista.get_element_by_index(indice)
        print(f'Capitana Marvel se llama {value.name}')
# b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.        
def guardianes(lista):
    cont = 0
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)

        if heroe.team == 'Guardianes de la Galaxia':
            cont += 1
            
            cola.arrive(heroe)
            # listag.insert(heroe)
        else:
            cont += 0
    return cont



# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.

def listadecreciente(lista):
    # lista.order_by(criterio="team")
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)

        if heroe.team == 'Guardianes de la Galaxia':
            lista1.insert((heroe), 'team')
        elif heroe.team == 'Los Cuatro Fantásticos':
            lista2.insert((heroe), 'team')

#  d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
def año_aparicion(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.year > 1960:
            print(
                f'El personaje {heroe.supername} aparecio despues de 1960')
        else:
            None

# e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.


def change_house(lista):
    indice = lista.search_r("Vlack Widow", 0, lista.size()-1, "supername")
    if indice != None:
        new_house = lista.get_element_by_index(indice)
        new_house.supername = 'Blanck Widow'
    lista.barrido()


# f. Dada una lista auxiliar con los siguientes personajes(‘Black
#  Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), agregarlos a la lista principal en el caso de no estar cargados.
# Lista 2
def cargalista_aux():
    lista_1.insert(Personajes("Loki", None, "Asgardians", 1949), "supername")
    lista_1.insert(Personajes("Rocket Raccoon", "Rocket","Guardians of the Galaxy", 1976), "supername")
    lista_1.insert(Personajes("Hulk", "Bruce Banner","Avengers", 1962), "supername")
    lista_1.insert(Personajes("Black Cat", "Felicia Hardy","Spiderman Allies", 1979), "supername")

def unir(lista, lista_1):
    for i in range(lista_1.size()):
        heroe = lista_1.get_element_by_index(i)
        lista.insert((heroe), 'supername')
# g. Mostrar todos los personajes que comienzan con C, P o S.


def first_c_p_s(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.supername[0] == 'C':
            print(f'La primer letra de {heroe.supername} es C')
        if heroe.supername[0] == 'P':
            print(f'La primer letra de {heroe.supername} es P')
        if heroe.supername[0] == 'S':
            print(f'La primer letra de {heroe.supername} es S')
        




superhéroes()
print()
print('--------------------------------------------------------------------')
print('Punto A')
capitana_marvel(lista)
print()
print('--------------------------------------------------------------------')
print('Punto B')
cont = guardianes(lista)
print(f'encontre {cont} personajes de los Guardianes de la Galaxia')
print()
print('--------------------------------------------------------------------')
print('Punto C')
listadecreciente(lista)
lista1.order_by(criterio="supername", reverse=True)
lista1.barrido()
print()
print('--------------------------------------------------------------------')
print()
lista2.order_by(criterio="supername", reverse=True)
lista2.barrido()
print()
print('--------------------------------------------------------------------')
print('Punto D')
año_aparicion(lista)
print()
print('--------------------------------------------------------------------')
print('Punto E')
change_house(lista)
print()
print('--------------------------------------------------------------------')
print('Punto F')
cargalista_aux()
unir(lista, lista_1)
lista.barrido()
print()
print('--------------------------------------------------------------------')
print('Punto G')
first_c_p_s(lista)
