import sys
ruta = 'D:/Users/leo_1/Documentos/inacap/Taller aplicacion/app/datos'
sys.path.append(ruta)
from db import *

class Habitacion(DB):
    def __init__(self,nHabitacion, idTipoHabitacion, capMax,capMin,orientacion,habilitar = 1):
        super().__init__()
        self.__nHabitacion = nHabitacion
        self.__idTipoHabitacion = idTipoHabitacion
        self.__capMax = capMax
        self.__capMin = capMin
        self.__orientacion = orientacion
    

    def verHabitacion(self):
        sql = "SELECT * FROM habitacion ORDER BY N_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("Numero habitacion " + str(x[0]))
                    print("Id tipo habitacion: " + str(x[1]))
                    print("Capacidad Maxima: " + str(x[2]))
                    print("Capacidad Minima: " + str(x[4]))
                    print("Orientacion: " + x[3])
                    print()
            else:
                print("No hay habitacion en la base de datos")

        except Exception as e:
            print("Error: ", e.args)

    def agregarHabitacion(self,numero,idTipoHabitacion,capMax,capMin,orientacion):
        val = (numero,idTipoHabitacion,capMax,orientacion,capMin)
        sql = "INSERT INTO habitacion (N_HABITACION, ID_TIPO_HABITACION,CAPACIDAD_MAX,ORIENTACION,MIN_PASAJERO) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('habitacion agregada')
        except Exception as e:
            print("Error: ", e.args)

    def modificarHabitacion(self,numero,idTipoHabitacion,capMax,capMin,orientacion):
        val = (idTipoHabitacion,capMax,orientacion,capMin,numero)
        sql = "UPDATE habitacion SET ID_TIPO_HABITACION = %s, CAPACIDAD_MAX = %s, ORIENTACION = %s, MIN_PASAJERO = %s WHERE N_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarHabitacion(self,numero):
        val = (numero)
        sql = "DELETE FROM habitacion WHERE N_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('la habitacion a sido eliminada')
        except Exception as e:
            print("Error: ", e.args)
