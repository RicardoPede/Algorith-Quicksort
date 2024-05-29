# Implementación del Algoritmo Quicksort en Python

###Objetivo
Implementar el algoritmo de ordenamiento Quicksort en Python utilizando el enfoque
de "divide y vencerás".
###Introducción
El objetivo de este trabajo práctico es comprender y aplicar el algoritmo Quicksort
para ordenar una lista de elementos. Quicksort es un algoritmo efciente y
ampliamente utilizado que se basa en la técnica de "divide y vencerás". Durante este
trabajo, se guiará paso a paso en la implementación del algoritmo, asegurando una
comprensión profunda de cada parte del proceso.
###Conceptos Clave
Divide y Vencerás: Técnica que divide un problema en subproblemas más pequeños
que son más fáciles de resolver.
Pivote: Elemento de la lista que se usa como referencia para dividir la lista en
sublistas.
Partición: Proceso de reorganizar los elementos de la lista de manera que los
menores que el pivote estén a su izquierda y los mayores a su derecha.
Recursión: Técnica en la que una función se llama a sí misma para resolver
subproblemas.
Caso Base: Condición que detiene la recursión, típicamente cuando la lista tiene 0 o 1
elementos.

## Pasos para la Implementación
● Defnición de la Función
Defne una función llamada quicksort que tome una lista.
● Caso Base
Dentro de la función, verifca si la sublista tiene 0 o 1 elementos (cuando el
índice de inicio es mayor o igual al índice de fn). Si es así, no hay nada que
ordenar y la función debe terminar.
● Selección del Pivote
Elige un elemento de la sublista como pivote. Un método simple es elegir el
primer elemento de la sublista.
● Partición de la Lista
Reorganiza los elementos de la sublista de manera que los menores que el
pivote estén a su izquierda y los mayores a su derecha.
● Colocación del Pivote
Coloca el pivote en su posición correcta de manera que todos los elementos a
su izquierda sean menores y todos los elementos a su derecha sean mayores.
● Llamadas Recursivas
Llama recursivamente a quicksort para las sublistas a la izquierda y a la
derecha del pivote.
● Combinación de Resultados
La lista se modifca en su lugar, por lo que no es necesario combinar listas
explícitamente.
● Prueba de la Implementación
Crea una lista de ejemplo y llama a la función quicksort para ordenarla.

## Actividades del Trabajo Práctico
### Defnir la Función Quicksort
Crea la función quicksort que tomará una lista.
### Implementar el Caso Base
Asegúrate de que la función maneje correctamente los casos en los que la sublista
tiene 0 o 1 elementos.
### Seleccionar y Colocar el Pivote
Implementa la selección del pivote y su colocación correcta después de la partición.
### Partición de la Lista
Escribe el código para particionar la lista en elementos menores y mayores que el
pivote.
### Recursión
Llama recursivamente a quicksort en las sublistas resultantes de la partición.
### Probar la Implementación
Prueba la función quicksort con una lista de ejemplo y verifca que se ordene
correctamente.
### Evaluación
Se evaluará la correcta implementación del algoritmo Quicksort en Python, la
comprensión de los conceptos clave, y la capacidad para optimizar el algoritmo.
Asegúrate de documentar tu código con comentarios explicativos y pruebas que
demuestren su funcionamiento correcto.
### Entrega
Código fuente de la implementación de Quicksort.
Documentación y comentarios explicativos en el código.
Ejemplos de pruebas con diferentes listas de entrada.