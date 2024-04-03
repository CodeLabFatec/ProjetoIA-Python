from pydantic import BaseModel, validator
from datetime import datetime, date

from models.handlers.date_utils import DateUtils

class informacoesDTO(BaseModel):

    id: int
    horario_entrada: datetime | None
    horario_saida: datetime | None
    data: date | None

    @validator('horario_entrada', 'horario_saida')
    def valida_data_hora(cls, value):
        return DateUtils.valida_data_hora(value)