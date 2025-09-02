# Definición de datos
ciudades = ["Ibarra", "Tulcan", "Quito"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 3

# Crear matriz 3D vacía: ciudad x día x semana
temperaturas = [
    [
        [0 for _ in range(semanas)]  # semanas
        for _ in dias               # días
    ]
    for _ in ciudades              # ciudades
]

# Ingreso manual de temperaturas
for i, ciudad in enumerate(ciudades):
    print(f"\nIngrese las temperaturas para {ciudad}:")
    for semana in range(semanas):
        print(f"  Semana {semana+1}:")
        for j, dia in enumerate(dias):
            temp = float(input(f"    {dia}: "))
            temperaturas[i][j][semana] = temp

# Cálculo de promedios por ciudad y semana
print("\n--- Promedio de Temperaturas ---")
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += temperaturas[i][dia][semana]
        promedio = suma / len(dias)
        print(f"  Semana {semana+1}: {promedio:.2f} °C")
