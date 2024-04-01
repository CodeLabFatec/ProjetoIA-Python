import os
from dotenv import load_dotenv
load_dotenv()

def selected_env():
    return os.getenv('FLASK_ENV')