import sys
ruta = 'D:/Users/leo_1/Documentos/inacap/Taller aplicacion/app/datos'
sys.path.append(ruta)
from db import *

class Registro(DB):
    def __init__(self,idRegistro,nHabitacion,rutPasajeroResponsable,fechaAsignacion,horaAsignacion,fechaFin,horaFin,nPersonas,costoAdicionalPersona,costoTotal):
        super().__init__()
        self.__idRegistro = idRegistro
        self.__nHabitacion = nHabitacion
        self.__rutPasajeroResponsable = rutPasajeroResponsable
        self.__fechaAsignacion = fechaAsignacion
        self.__horaAsignacion = horaAsignacion
        self.__fechaFin = fechaFin
        self.__horaFin = horaFin
        self.__nPersonas = nPersonas
        self.__costoAdicionalPersona = costoAdicionalPersona
        self.__costoTotal = costoTotal

    def verRegistro(self):
        sql = "SELECT * FROM registro ORDER BY ID_REGISTRO asc"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            if (len(datos) != 0):
                for x in datos:
                    print("Id registro " + str(x[0]))
                    print("Numero habitacion: " + str(x[1]))
                    print("Rut responsable: " + str(x[2]))
                    print("Fecha de asignacion: " + str(x[3]))
                    print("Hora de asignacion:" + x[4])
                    print("Fecha de termino:" + x[5])
                    print("Hora de finalizacion:" + x[6])
                    print("Numero de personas: "  + x[7])
                    print("Costo adicional por personas:" + x[8])
                    print("Costo Total" + x[9])
                    print()
            else:
                print("No hay registros en la base de datos")

        except Exception as e:
            print("Error: ", e.args)

    def agregarRegistro(self,idRegistro,nHabitacion,rutResponsable,fechaAsignacion,horaAsignacion,fechaFin,horaFin,nPersonas,costoAdicionaPer,costoTotal):
        val = (idRegistro,nHabitacion,rutResponsable,fechaAsignacion,horaAsignacion,fechaFin,horaFin,nPersonas,costoAdicionaPer,costoTotal)
        sql = "INSERT INTO registro (ID_REGISTRO, N_HABITACION,RUT_PASAJERO_RESPONSABLE,FECHA_ASIGNACION,HORA_ASIGNACION,FECHA_FIN,HORA_FIN,N_PERSONAS,COSTO_ADICIONAL_PERSONA,COSTO_TOTAL) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(sql,val)
            self.connect.commit()
            print('Registro agregada')
        except Exception as e:
            print("Error: ", e.args)