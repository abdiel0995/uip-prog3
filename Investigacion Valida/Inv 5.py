
nom = input ("Ingrese nombre de archivo con su extension, a abrir: ")
archivo = open(nom,"r")
contenido = archivo.read()
print(contenido)
