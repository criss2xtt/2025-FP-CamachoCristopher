# Escritura de Archivo de Texto
# Creamos (o sobrescribimos) el archivo 'my_notes.txt'
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Primera nota: Hoy aprendí sobre integración numérica.\n")
    file.write("Segunda nota: La práctica y retroalimentación mejoran la presentación oral.\n")
    file.write("Tercera nota: Python facilita el manejo de archivos de texto.\n")
# El archivo se cierra automáticamente al salir del bloque 'with'

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea usando readline()
    line = file.readline()  # Lee la primera línea
    while line:
        print(line.strip())  # Mostramos la línea sin salto de línea extra
        line = file.readline()  # Avanza a la siguiente línea
# El archivo se cierra automáticamente al salir del bloque 'with'
