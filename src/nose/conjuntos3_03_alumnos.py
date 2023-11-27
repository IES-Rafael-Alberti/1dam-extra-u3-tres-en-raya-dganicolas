"""
Ejercicio 3.3.3
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
"""

# TODO: Declara la función conjunto_potencia según la documentación que observas a continuación:
def lista(conjunto_original:set):
    """ Genera la lista de todos los subconjuntos posibles de un conjunto
    :param conjunto_original: conjunto del que debemos realizar la lista del conjunto potencia
    :type conjunto_original: set
    :returns: la lista del conjunto potencia resultante
    :rtype: list
    """
    # TODO: Inicializar la lista potencia con el conjunto vacío:
    lista_potencia=[set()]

    # TODO: Recorrer los elementos del conjunto original:
    for elemento in conjunto_original:

        # Explicación de qué vamos a hacer en el bucle:
        # Crear nuevos subconjuntos agregando el elemento actual a los subconjuntos 
        # existentes en la lista potencia mediante la operación de unión entre el 
        # elemento del conjunto original y cada subconjunto de la lista potencia.

        # TODO: Primero creamos una lista vacía que se llame nuevos_subconjuntos:
        nuevos_subconjuntos=[]
        # TODO: Ahora recorremos los subconjuntos de la lista potencia:
        for subconjunto in lista_potencia: 
            # TODO: Por cada iteración, agregamos a la lista nuevos_subconjuntos
            # la unión del subconjunto y el elemento 
            # (que debemos introducirlo en un conjunto para la operación unión):
            nuevos_subconjuntos.append(subconjunto|{elemento})
        
        # TODO: Agregar los nuevos subconjuntos a la lista potencia:
        lista_potencia.extend(nuevos_subconjuntos)

    # TODO: Retornar la lista creada con la lista de todos los subconjuntos
    return lista_potencia


def main():
    conjunto_original = {6, 1, 4}
    # TODO: Realiza la llamada a la función conjunto_potencia:
    conjuntos=lista(conjunto_original)
    # TODO: Muestra la lista resultante del conjunto potencia en consola:
    print(conjuntos)


if __name__ == "__main__":
    main()
