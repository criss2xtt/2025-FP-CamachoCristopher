# Crear el diccionario inicial con información ficticia
informacion_personal = {
    "nombre": "Juan Olmedo",
    "edad": 31,
    "ciudad": "Ibarra",
    "profesion": "Ingeniero en Sistemas"
}

# 1. Acceder y modificar el valor asociado con "ciudad"
informacion_personal["ciudad"] = "Quito"

# 2. Agregar una nueva clave-valor que represente la profesion (ya existe, pero vamos a actualizarla con otra)
informacion_personal["profesion"] = "Desarrollador de Software"

# 3. Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0984654823"

# 4. Eliminar la clave "edad", utilizando .pop y none
informacion_personal.pop("edad", None)  # usamos .pop con None para evitar error si no existe

# 5. Imprimir el diccionario final con for para que recorra cada clave y ejecute el codigo verticalmente
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

