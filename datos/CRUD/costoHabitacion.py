import sys
ruta = 'D:/Users/leo_1/Documentos/inacap/Taller aplicacion/app/datos'
sys.path.append(ruta)
from db import *

class costoHabitacion(DB):
    def  __init__(self,idCostoHabitacion,idTipoHabitacion,costoBase):
        super().__init__()
        self.__idCostoHabitacion = idCostoHabitacion
        self.__idTipoHabitacion = idTipoHabitacion
        self.__costoBase = costoBase

    def agregarCostoHabitacion(self,idCostoHabitacion,idTipoHabitacion,costoBase):
        val = (idCostoHabitacion,idTipoHabitacion,costoBase)
        sql = "INSERT INTO costo_habitacion (ID_COSTO_HABITACION, ID_TIPO_HABITACION,COSTO_BASE) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el costo de habitacion a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarCostoHabitacion(self,idCostoHabitacion):
        val = idCostoHabitacion
        sql = "DELETE FROM costo_habitacion WHERE ID_COSTO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el pasajero a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)
    
    def modificarCostoHabitacion(self,idCostoHabitacion,idTipoHabitacion,CostoBase):
        val = (idTipoHabitacion,CostoBase,idCostoHabitacion)
        sql = "UPDATE costo_habitacion SET ID_TIPO_HABITACION = %s , COSTO_BASE = %s  WHERE ID_COSTO_HABITACION = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def verCostoHabitacion(self):
        sql = "SELECT * FROM costo_habitacion ORDER BY ID_COSTO_HABITACION asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("Id costo habitacion: " + str(x[0]))
                    print("Id tipo habitacion: " + x[1])
                    print("costo base: " + x[2])
                    print()
            else:
                print("No hay costos asignados")

        except Exception as e:
            print("Error: ", e.args)

