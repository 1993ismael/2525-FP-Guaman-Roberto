# My notes
# Tarea: Escritura y Lectura de Archivos de Texto
# Autor: Ismael
# Descripción: Programa que crea un archivo de texto, escribe notas,
#              luego lee el archivo línea por línea y muestra el contenido en consola.

# Escritura en el archivo
# -----------------------
# Se abre el archivo 'my_notes.txt' en modo escritura ('w')
# Si no existe, se crea automáticamente.
archivo = open("my_notes.txt", "w")

# Se escriben varias líneas de texto usando write()
archivo.write("primera nota: Hoy aprendí a manejar archivos en Python.\n")
archivo.write("Segunda nota: La función write() sirve para escribir en un archivo.\n")
archivo.write("Tercera nota: La función readline() permite leer línea por línea.\n")

# Cerramos el archivo después de escribir
archivo.close()


# Lectura del archivo
# -------------------
# Se abre el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

print("Contenido del archivo my_notes.txt:\n")

# Leer línea por línea con readline()
linea = archivo.readline()
while linea:  # mientras la línea no esté vacía
    print(linea.strip())  # .strip() elimina el salto de línea extra
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()