


>>> li[ ]
>>> print("Lista de Supermercados")
>>> print("-------------------------------")
>>> op=input("1. Agregar elementos/n"+"2. Eliminar elementos/n"+"3. Ver todos los elementos")
>>> if op==1:
>>>    nom=input("Ingrese nuevo nombre")
>>>    li.append(nom)
>>> if op==2:
>>>    nom=input("Escriba nombre exacto a borrar")
>>>    del li[nom]
>>> if op==3:
>>>    print (li)
