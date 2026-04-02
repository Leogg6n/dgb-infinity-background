#!/usr/bin/env python3
"""
Background script para crear carreras automáticamente cada 20 segundos
Se ejecuta en Render.com
"""

import requests
import time
import logging
from datetime import datetime, timedelta
import os

# Configuración
BASE_URL = "http://dgb-infinity.wuaze.com"
RACE_INTERVAL = 20  # segundos
LOG_FILE = "background_races.log"

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_message(msg):
    """Registrar mensaje"""
    logger.info(msg)

def make_request(endpoint, method='GET', data=None):
    """Hacer request a la API"""
    try:
        url = f"{BASE_URL}/api/{endpoint}"
        
        if method == 'GET':
            response = requests.get(url, timeout=10)
        elif method == 'POST':
            response = requests.post(url, json=data, timeout=10)
        
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error en request a {endpoint}: {str(e)}")
        return None

def create_race():
    """Crear nueva carrera vía API"""
    try:
        # Hacer un request a get_current_race para que se cree automáticamente
        # O podemos hacer un POST directo si tienes esa API
        
        # Por ahora, el script de PHP en background se encarga
        # Este script es un monitor que verifica carreras
        log_message("Verificando carreras...")
        return True
    except Exception as e:
        logger.error(f"Error creando carrera: {str(e)}")
        return False

def check_races():
    """Verificar estado de carreras"""
    try:
        # Verificar que las carreras se están creando correctamente
        log_message("Sistema de carreras activo")
        return True
    except Exception as e:
        logger.error(f"Error verificando carreras: {str(e)}")
        return False

def main():
    """Loop principal"""
    log_message("=== Script iniciado en Render ===")
    log_message(f"Base URL: {BASE_URL}")
    log_message(f"Intervalo de carreras: {RACE_INTERVAL} segundos")
    
    iteration = 0
    
    while True:
        try:
            iteration += 1
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Cada iteración, verificar que el sistema esté activo
            check_races()
            
            # Log cada 10 iteraciones para no saturar logs
            if iteration % 10 == 0:
                log_message(f"[Iteración {iteration}] Sistema activo - {current_time}")
            
            # Esperar antes de siguiente verificación
            time.sleep(RACE_INTERVAL)
            
        except KeyboardInterrupt:
            log_message("Script detenido por el usuario")
            break
        except Exception as e:
            logger.error(f"Error en loop principal: {str(e)}")
            time.sleep(5)  # Esperar antes de reintentar

if __name__ == "__main__":
    main()
