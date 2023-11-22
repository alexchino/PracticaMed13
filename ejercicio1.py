#Diseña una clase llamada Biblioteca que utilice una pila para gestionar libros prestados.
#Implementa métodos para prestar, devolver y mostrar el estado de la pila. Crea una
#instancia de la clase y realiza operaciones de préstamo y devolución con libros específicos
#como "Cien años de soledad" o "Don Quijote de la Mancha". Imprime mensajes
#informativos para cada operación y muestra el estado de la pila después de ciertas
#acciones.

from random import randint

def dados():
    """
    Función que simula lanzar dados.
    Retorna una tupla con dos números enteros aleatorios
    """
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

def pedir_accion():
    """
    Función que solicita al usuario que elija una acción.
    Retorna un string con la acción elegida
    """
    print("¿Qué deseas hacer?")
    print("1. Lanzar dados")
    print("2. Salir")
    accion = input("Escribe el número de la acción: ")
    return accion

def mostrar_resultado(resultado):
    """
    Función que muestra el resultado de lanzar dados.
    """
    print(f"¡Los resultados son {resultado[0]} y {resultado[1]}!")

def main():
    while True:
        accion = pedir_accion()
        if accion == "1":
            resultado = dados()
            mostrar_resultado(resultado)
        elif accion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Accion no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

