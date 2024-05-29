def quicksort(lista):
    if len(lista) <= 1:         # Manejo para listas vacias o con un solo elemento
        return lista
    pivot = lista[len(lista) // 2] # Seleccionamos el pivote
    # Particionamos la lista en tres partes
    # Menores, iguales y mayores al pivote
    # Para cada elemento x en lista, si x es menor que pivot, entonces x se incluirá en la nueva lista.
    left = [x for x in lista if x < pivot] 
    # Para cada elemento x en lista, si x es igual que pivot, entonces x se incluirá en la nueva lista.
    middle = [x for x in lista if x == pivot] 
    # Para cada elemento x en lista, si x es mayor que pivot, entonces x se incluirá en la nueva lista.
    right = [x for x in lista if x > pivot] 
    # Recursivamente ordenamos las listas
    # Concatenamos las listas ordenadas
    return quicksort(left) + middle + quicksort(right)

lista = [ 3, 6, 8, 10, 1, 2, 1, -1 ]

print(quicksort(lista))
