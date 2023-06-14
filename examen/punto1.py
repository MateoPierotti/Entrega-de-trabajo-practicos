# 1. Desarrollar una función recursiva que permita contar cuantas veces
# aparece una determinada palabra, en un vector de palabras.
palabras = ['chau', 'chau', 'francia', 'teclado', 'chau']
buscada = 'chau'

def cuantas(que, vector):
    if not vector:
        return 0 
    elif vector[0] == que:
        return cuantas(que, vector[1:]) + 1
    else:
        return cuantas(que, vector[1:])


print(cuantas(buscada, palabras))
