# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
# treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

# a. mostrar los nombre películas estrenadas en el año 2014
# b. indicar cuántas películas se estrenaron en el año 2018
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
from pila import Pila


class Pelicula:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year


stack = Pila()

#! Carga

stack.push(Pelicula('El amanecer del planeta de los simios',
           'Chernin Entertainment', 2014))
stack.push(Pelicula('El Sorprendente Hombre Araña 2', 'Sony Pictures', 2014))
stack.push(Pelicula('Los increíbles 2', 'Walt Disney Pictures', 2018))
stack.push(Pelicula('Jurassic World: el reino caído',
           'Perfect World Pictures', 2018))
stack.push(Pelicula('Deadpool', 'Marvel Studios', 2016))
stack.push(Pelicula('Doctor Strange: hechicero supremo', 'Marvel Studios', 2016))
# stack.push(Pelicula('Doctor Strange: hechicero supremo', 'Marvel Studios', 2015))
# stack.push(Pelicula('Doctor Strange: hechicero supremo', 'Marvel Studios', 2016))
# stack.push(Pelicula('Doctor Strange: hechicero supremo', 'Marvel Studios', 2016))
# stack.push(Pelicula('Doctor Strange: hechicero supremo', 'Marvel Studios', 2016))
pelis_en_2018 = 0

while stack.size() > 0:
    if stack.on_top().year == 2014:
        print()
        print(f'Pelicula estrenada en el 2014: { stack.on_top().name}')
        print()
        
    if stack.on_top().year == 2018:
        pelis_en_2018 += 1
        # print(stack.on_top().name)

    if stack.on_top().year == 2016 and stack.on_top().make == 'Marvel Studios':
        print()
        print(f'Pelicula de Marvel Studios y estrenada en el 2016: { stack.on_top().name}')
        print()
        
    stack.pop()
print()
print(f'{pelis_en_2018} peliculas se estrenaron en 2018')
print()
