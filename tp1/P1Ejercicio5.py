def numeros_romano(nromano):
    """ingresar numeros romanos"""

    # diccionario
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # nromano = 0
    if len(nromano) == 0:
        return 0
    # nromano = 1
    elif len(nromano) == 1:
        return valores[nromano]
    # elif valores[nromano[1]] < valores[nromano[2]]:
    #     valor = valores[nromano[2]] - valores[nromano[1]]
    #     return valor + valores[nromano[0]] + numeros_romano(nromano[2:])
    # nromano 1 < 2
    elif valores[nromano[0]] < valores[nromano[1]]:
        return valores[nromano[1]] - valores[nromano[0]] + numeros_romano(nromano[2:])
    else:
        return valores[nromano[0]] + numeros_romano(nromano[1:])


print(numeros_romano(input('Ingrese un numero romano en mayuscula: ')))
