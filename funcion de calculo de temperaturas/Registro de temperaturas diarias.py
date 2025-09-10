import random

# Definición de datos
ciudades = ["Ibarra", "Tulcán", "Quito"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear matriz 3D: ciudad x semana x día
# Cada celda almacena la temperatura de una ciudad en un día específico de una semana
temperaturas = [
    [
        [random.randint(10, 30) for _ in dias]   # días
        for _ in range(semanas)                 # semanas
    ]
    for _ in ciudades                           # ciudades
]

# Función para calcular los promedios de temperatura por ciudad
def promedio_temperaturas(temperaturas, ciudades, semanas, dias):
    """
    Calcula el promedio de temperaturas por ciudad.
    Recorre la matriz 3D (ciudad -> semana -> día) con bucles anidados.
    """
    print("\n--- Promedio de Temperaturas por Ciudad ---")
    for i, ciudad in enumerate(ciudades):
        suma = 0
        contador = 0
        for semana in range(semanas):           # recorrer semanas
            for dia in range(len(dias)):        # recorrer días
                suma += temperaturas[i][semana][dia]
                contador += 1
        promedio = suma / contador if contador > 0 else 0
        print(f"{ciudad}: {promedio:.2f} °C")

# Mostrar datos generados (para verificar la matriz)
print("\n--- Datos de temperaturas generados ---")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for semana in range(semanas):
        print(f"  Semana {semana+1}: {temperaturas[i][semana]}")








