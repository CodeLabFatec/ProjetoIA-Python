from typing import Literal, Union
from pydantic import BaseModel, BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

class DevConfig(BaseSettings):
    env: Literal['dev']
    MYSQL_URL: str = os.getenv('DATABASE_URL')

class TestConfig(BaseSettings):
    env: Literal['test']
    MYSQL_URL: str = os.getenv('DATABASE_URL')

class ProdConfig(BaseSettings):
    env: Literal['prod']
    MYSQL_URL: str = os.getenv('DATABASE_URL')

class Config(BaseModel):
    config: Union[DevConfig, TestConfig, ProdConfig]

