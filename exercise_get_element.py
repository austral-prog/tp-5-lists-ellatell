# Ejercicio 2: Obtener elemento en posición específica

def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor mínimo de la lista o None si está vacía
    """
    if len(lista) == 0:
        return None
    return min(lista)
