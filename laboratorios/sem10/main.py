import libro, autor, lector, copia


op=0
es=10
li=[]
li2=[]
li3=[]
print ("\t\tMenu\n1. Ingresar lector\n2. Ingresar Autor\n3. Ingresar Libro\n4. Hacer peticion\n5. Hacer devolucion")
op=input("Seleccione...")

while op<6:
if op==1:
	id=input("Ingrese el id del lector")
	no=input("Ingrese el nombre del lector")
	ob1=lector.Lector(id, no)
	li.append=[ob1]
elif op==2:
	no=input("Ingrese el nombre del autor")
	nac=input("Ingrese nacionalidad")
	ob2=autor.Autor(no, nac)
	li2.append=[ob2]
	
	
elif op==3:
	tit=input("Ingrese titulo de libro")
	tip=input("Ingrese tipo de libro")
	edi=input("ingrese editorial del libro")
	ob3=libro.Libro(tit, tip, edi)
	li3.append=[ob3]
	
elif op==4:
	print("Haciendo peticion...")
	ob4=copia.Copia(id, es)
	es==-1
	
elif op==5:
	print("Haciendo Devolucion...")
	
	es==+1
	
