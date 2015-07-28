import cx_Oracle
conectar=cx_Oracle.connect("abdiel/host@127.0.0.1/oracle")
print (conectar.version)
conectar.close()
