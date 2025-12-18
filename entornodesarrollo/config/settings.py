from dotenv import load_dotenv
import os
from pathlib import Path

# Cargar archivo .env desde la carpeta config

load_dotenv('entornodesarrollo/config/.env')

def get_env_variable(key: str, required: bool = True):
    value = os.getenv(key)
    if required and not value:
        raise EnvironmentError(f"La variable requerida '{key}' no está definida en el archivo .env")
    return value

# SAP
SAP_CONFIG = {
    'SAP_USUARIO': get_env_variable('SAP_USUARIO'),
    'SAP_PASSWORD': get_env_variable('SAP_PASSWORD'),
    'SAP_CLIENTE': get_env_variable('SAP_CLIENTE'),
    'SAP_IDIOMA': get_env_variable('SAP_IDIOMA'),
    'SAP_PATH': get_env_variable('SAP_PATH'),
    'SAP_SISTEMA': get_env_variable('SAP_SISTEMA')
}

# RUTAS
RUTAS = {
    'PATH_PROYECTO': get_env_variable('PATH_PROYECTO'),
    'PATH_AUDIT': get_env_variable('PATH_AUDIT'),
    'PATH_LOGS': get_env_variable('PATH_LOGS'),
    'PATH_TEMP': get_env_variable('PATH_TEMP'),
    'PATH_INSUMO': get_env_variable('PATH_INSUMO'),
    'PATH_RESULTADO': get_env_variable('PATH_RESULTADO')
}
print("RUTAS:", RUTAS)
print("SAP_CONFIG:", SAP_CONFIG)

