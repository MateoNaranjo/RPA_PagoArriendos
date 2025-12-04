import os
import logging as lg


class DepliegueAmbiente:

    def __init__(self):

        self.path_proyecto = "C:/ProgramData/RPA_PagoArriendos"
        self.path_audit = "C:/ProgramData/RPA_PagoArriendos/Audit"
        self.path_logs = "C:/ProgramData/RPA_PagoArriendos/Audit/Logs"
        self.path_temp ="C:/ProgramData/RPA_PagoArriendos/Temp"
        self.path_insumo = "C:/ProgramData/RPA_PagoArriendos/Insumo"
        self.path_resultado = "C:/ProgramData/RPA_PagoArriendos/Resultado"

    def crearCarpetas (self):
    
        try:
            for carpeta in [
                self.path_proyecto,
                self.path_audit,
                self.path_logs,
                self.path_temp,
                self.path_insumo,
                self.path_resultado
            ]:
                if not os.path.exists(carpeta):
                    os.mkdir(carpeta)
                    print(f"Carpeta creada con éxito: {carpeta}")
            
                else:
                    print(f"Carpeta de {carpeta} ya existe")

                ejecucionPrueba=DepliegueAmbiente()
                ejecucionPrueba.audit_log('El despliegue de ambiente fue exitoso ', 'Despliegue de ambiente')
            
        except Exception as e:
            ejecucionPrueba=DepliegueAmbiente()
            ejecucionPrueba.error_log('Ocurrio un error en la funcion (crearCarpte) en el archivo: ', 'DespliegueAmbiente')

    def audit_log(self, message, name_file):
        
        lg.basicConfig(filename=self.path_logs+'/example.log', encoding='utf-8', level=lg.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        lg.info(f'{message}. {name_file}')

    def error_log(self, message, name_file):

        lg.basicConfig(filename='example.log', encoding='utf-8', level=lg.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        lg.info(f'{message}. {name_file}')
        
ejecucionPrueba=DepliegueAmbiente()

ejecucionPrueba.audit_log('se inicio la subtarea', 'Despliegue de ambiente')