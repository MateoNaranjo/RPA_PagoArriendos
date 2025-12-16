import win32com.client
import pythoncom
import time
import os
import sys
import subprocess
from config.settings import SAP_CONIFG, RUTAS

class PagoArriendos:

    def __init__(self, usuariosSAP, contrasenaSAP, clienteSAP, idiomaSAP, aplicativoSAP,sistemaSAP):
        self.usuarioSAP= usuariosSAP
        self.contrasenaSAP=contrasenaSAP
        self.clienteSAP=clienteSAP
        self.idiomaSAP=idiomaSAP
        self.aplicativoSAP=aplicativoSAP
        self.sistemaSAP=sistemaSAP

    def abrir_SAP(self):
        try:
            
            win32com.client.GetObject("SAPGUI")
            print("SAP GUI ya está en ejecución.")
        except:
            
            try:
                print(f"Iniciando SAP GUI desde: {self.aplicativoSAP}")
                subprocess.Popen(self.aplicativoSAP)
                time.sleep(5)
            except FileNotFoundError:
                print(f"ERROR: No se encontró el ejecutable en la ruta: {self.ruta_aplicativoSAP}")
                return False
            except Exception as e:
                print(f"ERROR al iniciar SAP GUI: {e}")
                return False
        return True

    # Modificación en el método conectar_SAP:

    def conectar_SAP(self):

        if not self.abrir_SAP():
            return None # Falló la apertura del GUI

        try:
            # 1. Obtener el objeto de automatización
            SapGuiAuto = win32com.client.GetObject("SAPGUI")
            if not SapGuiAuto:
                raise Exception("No se pudo obtener el objeto SAPGUI (SAP Scripting Engine).")
                
            application = SapGuiAuto.GetScriptingEngine
            
            # 2. Abrir la conexión al sistema
            print(f"Intentando abrir conexión con: {self.sistemaSAP}")
            # El 'True' es para asegurar que se use el sistema de un solo track
            connection = application.OpenConnection(self.sistemaSAP, True)
            time.sleep(2) # Esperar a que la ventana de login aparezca

            # 3. Obtener la sesión activa
            sesion = connection.Children(0)
            return sesion
        except Exception as e:
            print(e)

    def ingresar_SAP(self, sesion):
        """Realiza el login. Si la sesión existe, intenta el login (sin validación de estado)."""
        
        sesion.findById("wnd[0]").maximize()
        sesion.findById("wnd[0]/usr/txtRSYST-BNAME").text = self.usuarioSAP
        sesion.findById("wnd[0]/usr/pwdRSYST-BCODE").text = self.contrasenaSAP
        sesion.findById("wnd[0]/usr/txtRSYST-MANDT").text = self.clienteSAP
        sesion.findById("wnd[0]").sendVKey(0)
       


ejecutarMain=PagoArriendos(SAP_CONIFG.get('SAP_USUARIO'),
                           SAP_CONIFG.get('SAP_PASSWORD'),
                           SAP_CONIFG.get('SAP_CLIENTE'),
                           SAP_CONIFG.get('SAP_IDIOMA'),
                           SAP_CONIFG.get('SAP_PATH'),
                           SAP_CONIFG.get('SAP_SISTEMA')
                           )

ejecutarMain.abrir_SAP()

