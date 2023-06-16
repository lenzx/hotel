import sys
ruta = 'D:/Users/leo_1/Documentos/inacap/Taller aplicacion/app/datos'
sys.path.append(ruta)
from db import *

class TipoHabitacion(DB):
    def __init__(self,idTipoHabitacion,TipoHabitacion):
        super().__init__()
        self.__idTipoHabitacion = idTipoHabitacion
        self.__TipoHabitacion = TipoHabitacion
        
    def agregarTipoHabitacion(self,id,nombre):
        val = (id,nombre)
        sql = "INSERT INTO tipo_habitacion (ID_TIPO_HABITACION, TIPO_HABITACION) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
        except Exception as e:
            print("Error: ", e.args)

    def verTipoHabitacion(self):
        sql = "SELECT * FROM tipo_habitacion ORDER BY ID_TIPO_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("ID_Tipo_Habitacion: " + str(x[0]))
                    print("Tipo_Habitacion: " + x[1])
                    print()
            else:
                print("No hay Tipos de habitaciones registrados")

        except Exception as e:
            print("Error: ", e.args)

    def modificarTipoHabitacion(self,id,nuevoValor):
        val = (nuevoValor,id)
        sql = "UPDATE TIPO_HABITACION SET TIPO_HABITACION = %s WHERE ID_TIPO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)



