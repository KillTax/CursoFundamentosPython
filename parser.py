fileref = open("ejemplo.txt", "r")
texto = fileref.readlines()
print(texto)


cadena2 = "soy una cadena con \n un salto de linea"
def contar_saltos_linea(cadena):
    return cadena.count("\n")
numero_saltos = contar_saltos_linea(cadena2)

print(f"{numero_saltos}")
fileref.close()