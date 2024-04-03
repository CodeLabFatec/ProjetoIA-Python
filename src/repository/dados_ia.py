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

    def get_informacoes_for_export(data_inicial : str, data_final : str) -> list[dict]:

        query_informacoes = db.session.query(
            informacoesEntity.id,
            informacoesEntity.horario_entrada,
            informacoesEntity.horario_saida,
            informacoesEntity.data,
        ).filter(
            informacoesEntity.data.between(data_inicial, data_final)
        )

        resultado_filtragem = {
            "informacoes":[
                {
                    'id': value.id,
                    'horario_entrada': value.horario_entrada,
                    'horario_saida': value.horario_saida,
                } for value in query_informacoes
            ]
        }
        return resultado_filtragem