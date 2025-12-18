import os
import logging as lg
import smtplib as sm
from email.mime.text import MIMEText
from config.settings import RUTAS


class Reutilizables:

    def __init__(self, path_proyecto, path_audit, path_logs, path_temp, path_insumo, path_resultado):

        self.path_proyecto = path_proyecto
        self.path_audit = path_audit
        self.path_logs = path_logs
        self.path_temp =path_temp
        self.path_insumo = path_insumo
        self.path_resultado = path_resultado

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

                
            self.audit_log('El despliegue de ambiente fue exitoso ', 'Despliegue de ambiente')
            
        except Exception as e:
            
            print(e)

    def audit_log(self, message, name_file):
        
        lg.basicConfig(filename=self.path_logs+'/example.log', encoding='utf-8', level=lg.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        lg.info(f'{message}. {name_file}')

    def error_log(self, message, name_file):

        lg.basicConfig(filename='example.log', encoding='utf-8', level=lg.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        lg.info(f'{message}. {name_file}')

    def Enviar_notificacion(self):
        pass
        
ejecucionPrueba=Reutilizables(RUTAS.get('PATH_PROYECTO'), RUTAS.get('PATH_AUDIT'), RUTAS.get('PATH_LOGS'), RUTAS.get('PATH_TEMP'), RUTAS.get('PATH_INSUMO'), RUTAS.get('PATH_RESULTADO'))
ejecucionPrueba.crearCarpetas()
ejecucionPrueba.audit_log('se inicio la subtarea', 'Despliegue de ambiente')
