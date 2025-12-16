from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv('config/.env')

def get_env_variable(key: str, required: bool = True):
    value = os.getenv(key)

    if required and not value:
        raise EnvironmentError(f"La variable '{key}' no está definida en .env")

    return value

#SAP

SAP_CONIFG={
    'SAP_USUARIO':get_env_variable('SAP_USUARIO'),
    'SAP_PASSWORD':get_env_variable('SAP_PASSWORD'),
    'SAP_CLIENTE':get_env_variable('SAP_CLIENTE'),
    'SAP_IDIOMA':get_env_variable('SAP_IDIOMA'),
    'SAP_PATH':get_env_variable('SAP_PATH'),
    'SAP_SITEMA':get_env_variable('SAP_SISTEMA')
}
#RUTAS

RUTAS={
    'PATH_PROYECTO':get_env_variable('PATH_PROYECTO'),
    'PATH_AUDIT':get_env_variable('PATH_AUDIT'),
    'PATH_LOGS':get_env_variable('PATH_LOGS'),
    'PATH_TEMP':get_env_variable('PATH_TEMP'),
    'PATH_INSUMO':get_env_variable('PATH_INSUMO'),
    'PATH_RESULTADO':get_env_variable('PATH_RESULTADO')
}
print(RUTAS)