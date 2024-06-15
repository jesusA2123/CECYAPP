import mysql.connector

class Conexion:
    def ConexionBD():
        try:
           
           conexion= mysql.connector.Connect(user='root', password='',
                                   host= 'localhost',database='cecyapp',port='3306')
           print('conexion correcta')
           return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos{}".format(error))
            return conexion
        
    ConexionBD()