from random import randint

objeto = ['botiquin', 'racion', 'botella',
          'blaster', 'linterna', 'casco de mandalor', 'partes de un robot', 'hologramas', 'mano bionica de look skywalker']


def lafuerza(mochila, error, objeto_extraido=0):

    if mochila == 1:
        print(
            f'se encontro el sable de luz en la posicion {objeto_extraido + 1}')

        return mochila
    elif error == 1:
        print('no se encontro el sable de luz')

    else:
        numero = 0
        numero = (randint(0, 8))
        print(
            f'se encontro un {objeto[ numero ]} en la posicion {objeto_extraido + 1}')

        return lafuerza(mochila - 1, error - 1, objeto_extraido+1)


lafuerza(mochila=(randint(1, 6)), error=(randint(4, 6)))
