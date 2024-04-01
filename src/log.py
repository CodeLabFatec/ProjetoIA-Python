import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging_level=os.getenv('LOGGING_LEVEL')
level_do_log = ''

if logging_level == 'info':
    level_do_log=logging.INFO
else:
    level_do_log=logging.DEBUG

formatar = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(encoding='utf-8', level=level_do_log, format=formatar,  datefmt="%d/%m/%Y %H:%M:%S")