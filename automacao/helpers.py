import os
from dotenv import load_dotenv
from loguru import logger

logger.remove()
logger.add(lambda m: print(m, end=''))

def log(message):
    logger.info(message)

def load_env():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base, '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        load_dotenv()
    config = {
        'SEATALK_WEBHOOK_URL': os.getenv('SEATALK_WEBHOOK_URL'),
        'SEATALK_PUBLIC_URL': os.getenv('SEATALK_PUBLIC_URL'),
        'SEATALK_SECRET_TOKEN': os.getenv('SEATALK_SECRET_TOKEN'),
        'ALMOX_URL_LOGIN': os.getenv('ALMOX_URL_LOGIN'),
        'ALMOX_URL_DASHBOARD': os.getenv('ALMOX_URL_DASHBOARD'),
        'ALMOX_USER': os.getenv('ALMOX_USER'),
        'ALMOX_PASSWORD': os.getenv('ALMOX_PASSWORD'),
        'CHROME_DRIVER_PATH': os.getenv('CHROME_DRIVER_PATH'),
        'BINARY_LOCATION': os.getenv('BINARY_LOCATION'),
        'CHROME_USER_PROFILE': os.getenv('CHROME_USER_PROFILE'),
        'PAGE_LOAD_TIMEOUT': int(os.getenv('PAGE_LOAD_TIMEOUT', '20')),
        'ELEMENT_TIMEOUT': int(os.getenv('ELEMENT_TIMEOUT', '15')),
        'RUN_MODE': os.getenv('RUN_MODE', 'visible')
    }

    return config
