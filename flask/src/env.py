from typing import Literal, Union
from pydantic import BaseModel, BaseSettings

class DevConfig(BaseSettings):
    env: Literal['dev']
    MYSQL_URL: str = 'mysql+pymysql://root:root@localhost'

class TestConfig(BaseSettings):
    pass

class ProdConfig(BaseSettings):
    pass

class Config(BaseModel):
    config: Union[DevConfig, TestConfig, ProdConfig]

