# Ejemplo de diccionario en Python
estudiante = {
    "nombre": "Ismael",
    "edad": 22,
    "carrera": "Ingeniería en Sistemas",
    "ciudad": ["loja"],
    "activo": True
}

# Mostrar todo el diccionario
print(estudiante)

# Acceder a un valor específico
print("Nombre:", estudiante["nombre"])
print("Carrera:", estudiante["carrera"])

# Agregar un nuevo par clave-valor
estudiante["semestre"] = 4

# Modificar un valor existente
estudiante["edad"] = 23

# Eliminar un elemento
del estudiante["activo"]

# Mostrar el diccionario actualizado
print(estudiante)