# busqueda_matriz.py

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]

def buscar_valor(matriz, valor):
    """
    Busca un valor dentro de la matriz.
    Retorna la posición (fila, columna) si lo encuentra, o None si no está.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Valor a buscar
valor_buscado = 25

# Llamamos a la función
posicion = buscar_valor(matriz, valor_buscado)

# Mostramos resultados
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
