# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [34, 12, 25],
    [78, 56, 10],
    [5,  99, 42]
]

# Función para mostrar la matriz de forma bonita
def mostrar_matriz(m):
    for fila in m:
        print(fila)

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, indice_fila):
    fila = matriz[indice_fila][:]  # Copiamos la fila seleccionada
    n = len(fila)

    # Algoritmo Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Reemplazamos la fila original con la fila ordenada
    matriz[indice_fila] = fila

print("📌 Matriz original:")
mostrar_matriz(matriz)

# Fila que queremos ordenar (por ejemplo, la fila 1 = segunda fila)
indice_fila_a_ordenar = 0

# Ordenamos esa fila
ordenar_fila(matriz, indice_fila_a_ordenar)

print("\n✅ Matriz después de ordenar la fila", indice_fila_a_ordenar)
mostrar_matriz(matriz)

