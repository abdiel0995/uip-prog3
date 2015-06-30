tx=""

opt=0
dic={}
lio=[]
lic=[]
c=0
print ("\t\tCifrado de mensajes")
print ("\n\n1.Introducir Texto\n2.Imprimir texto\n")
opt=input("Seleccione una opcion: ")
"""Funcion dependiendo de la seleccion"""
"""Aqui el compilador no me ejecuto el IF, porque? no se. Probe con otro codigo
subido a github ya comprobado y tampoco"""
if opt==1:
    tx=input("Ingrese cadena de texto :  ")
    op=input("1.Cifrar\n2.Descifrar")
"""Inicio de cifrado"""
    if op==1:
        print("Cifrando texto...")
        for i in tx:
            un=ord(i)
            lic.append(un)
            lio.append(i)
            print (lic)
"""Descifrando"""
    if op==2:
        print("Descifrando texto...")
        for i in tx:
            un=chr(i)
            lic.append(un)
            lio.append(i)
            print (lio)
"""Imprimiendo cadena de texto"""
if opt==2:
            print (tx)

    

    
    
