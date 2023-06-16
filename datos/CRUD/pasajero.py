import sys
ruta = 'D:/Users/leo_1/Documentos/inacap/Taller aplicacion/app/datos'
sys.path.append(ruta)
from db import *

class pasajero(DB):
    def __init__(self,rutPasajero,nombre):
        super().__init__()
        self.__rutPasajero = rutPasajero
        self.__nombre = nombre
    
    def agregarPasajero(self,rut,nombre):
        val = (rut,nombre)
        sql = "INSERT INTO pasajero (RUT_PASAJERO, NOMBRE) VALUES (%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el pasajero a sido agregado')
        except Exception as e:
            print("Error: ", e.args)

    def quitarPasajero(self,rut):
        val = (rut)
        sql = "DELETE FROM pasajero WHERE RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('el pasajero a sido eliminado')
        except Exception as e:
            print("Error: ", e.args)

    def modificarPasajero(self,rut,nuevoNombre):
        val = (nuevoNombre,rut)
        sql = "UPDATE pasajero SET NOMBRE = %s WHERE RUT_PASAJERO = %s"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('cambio realizado')
        except Exception as e:
            print("Error: ", e.args)

    def verPasajero(self):
        sql = "SELECT * FROM pasajero ORDER BY RUT_PASAJERO asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("Rut pasajero: " + str(x[0]))
                    print("Nombre: " + x[1])
                    print()
            else:
                print("No hay pasajeros registrados")

        except Exception as e:
            print("Error: ", e.args)
            
    def verPasajeroRut(self,rut):
        val = rut
        sql = "SELECT * FROM pasajero WHERE RUT_PASAJERO = %s "
        try:
            self.cursor.execute(sql,val)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("Rut pasajero: " + str(x[0]))
                    print("Nombre: " + x[1])
                    print()
            else:
                print("No hay pasajeros registrados")

        except Exception as e:
            print("Error: ", e.args)
pasajero('111111','jose salgado').verPasajeroRut('222222')
