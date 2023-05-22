from cola import Cola
from pila import Pila

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#   de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#   resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#   la palabra ‘Python’, si perder datos en la cola

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#   11: 43 y las 15: 57, y determinar cuántas son.


class Smartphone:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje


cola = Cola()
colaface = Cola()
colatwitter = Cola()
pila = Pila()


def notification():
    cola.arrive(Smartphone(10.34, "Instragram", "nuevo seguidor"))
    cola.arrive(Smartphone(11.12, "Facebook", "No leiste el mensaje"))
    cola.arrive(Smartphone(11.30, "Facebook", "Es el cumpleaños de Juan Carlos"))
    cola.arrive(Smartphone(12.15, "Twitter", "usa Python es gratis"))
    cola.arrive(Smartphone(12.43, "Twitter", "#boladefraile"))
    cola.arrive(Smartphone(13.58, "Instragram", "nuevo seguidor"))
    cola.arrive(Smartphone(11.45, "WhatsApp", "Como que no?"))
    cola.arrive(Smartphone(13.00, "Pinterest", "Tatuajes que pueden gustarte"))
    cola.arrive(Smartphone(12.43, "Twitter", "Sabias todo esto sobre Python"))
    cola.arrive(
        Smartphone(
            13.58,
            "Twitter",
            "Lenjuages de programacion que pueden agradarte: Java, Python, C++",
        )
    )
    cola.arrive(Smartphone(11.45, "Facebook", "nueva notificacion"))
    cola.arrive(Smartphone(14.15, "Instagram", "34 likes en tu publicacion"))


# eliminar facebook


def notface(cola):
    while cola.size() > 0:
        if cola.on_front().aplicacion == "Facebook":
            cola.atention()

        else:
            print(
                f"{cola.on_front().aplicacion}: {cola.on_front().mensaje} / Hora: {cola.on_front().hora}"
            )
            cola.atention()


# twitter python


def twitterpython(cola):
    while cola.size() > 0:
        if cola.on_front().aplicacion == "Twitter" and (
            "Python" in cola.on_front().mensaje
        ):
            print(
                f"Se encontro en twitter una notificacion con una referencia a Python a las {cola.on_front().hora}"
            )
            print(f"La referencia era: {cola.on_front().mensaje}")
            cola.atention()

        else:
            cola.atention()


def horasnoti(cola, pila):
    cont = 0

    while cola.size() > 0:
        if (cola.on_front().hora >= 11.43) and (cola.on_front().hora < 15.57):
            cosa = cola.atention()

            pila.push(cosa)
            cont += 1
            # print(f'llevan {cont} notificaciones')
        else:
            cola.atention()
    return cont


print()
print("--------------------------------------------------------------------")
print("Notificaciones escluyendo a Facebook")
print()
notification()
notface(cola)
print()
print("--------------------------------------------------------------------")
print("Notificaciones de Twitter con referencia a Python")
print()
notification()
twitterpython(cola)
print()
print("--------------------------------------------------------------------")
print("Cuantas notificaciones llegaron Entre las 11:43 y las 15:57")
print()
notification()
horasnoti(cola, pila)
print(f"llegaron {pila.size()} notificaciones")
print()
