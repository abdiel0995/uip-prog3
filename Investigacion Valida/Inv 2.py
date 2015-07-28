import socket
nombre_equipo = socket.gethostname()
direccion_equipo = socket.gethostbyname(socket.gethostname())
print (direccion_equipo)
