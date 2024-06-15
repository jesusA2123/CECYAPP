from conexion import *

class Consultas:
 
 def registrarUsuario(nombre,correo,contraseña):

  try:
    cone= Conexion.ConexionBD()
    cursor=cone.cursor()
    sql = "INSERT INTO registros VALUES (%s,%s,%s);" #Consulta para agregar cursos

    valores = (nombre,correo,contraseña)
    cursor.execute(sql,valores)
    cone.commit()
    print(cursor.rowcount, "Registro ingresado")
    cone.close()
          
  except mysql.connector.Error as error:
    print("Error al agregar datos{}".format(error))

 def inicioSesion(nombre, correo,contraseña):
  try:
    cone= Conexion.ConexionBD()
    cursor=cone.cursor()
    sql = "SELECT nombre FROM registros WHERE correo = %s AND contraseña = %s;" #Consulta para buscar usuario

    valores = (correo, contraseña)  # Solo correo y contraseña se usan en la consulta
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()  # Obtener un solo resultado

    cone.close()

    if resultado:
        print(f"{cursor.rowcount} Usuario encontrado")
        return True
    else:
        print("El usuario no se encuentra en la BD")
        return False

  except mysql.connector.Error as error:
        print("Error en la base de datos: {}".format(error))
        return False
  

  
 
  