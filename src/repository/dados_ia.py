from models.dto.informacoes import informacoesDTO
from entities.dados_ia import informacoesEntity

from app import db

class informacoesRepository:
    
    @staticmethod
    def get_all():
        return [informacoesDTO(**dados.__dict__).__dict__ for dados in informacoesEntity.query.all()]
    
    @staticmethod
    def save(informacoes):
        db.session.add(informacoes)
        db.session.flush()
        db.session.refresh(informacoes)
        return informacoes.id