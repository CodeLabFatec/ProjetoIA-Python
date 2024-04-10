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

    def get_informacoes_for_export(data_entrada) -> dict:

        query_informacoes = db.session.query(
            informacoesEntity.id,
            informacoesEntity.data_entrada,
            informacoesEntity.data_saida,
            informacoesEntity.hora_entrada,
            informacoesEntity.hora_saida
        ).filter_by(
            informacoesEntity.data_entrada == data_entrada
        )

        data_inicial_anterior = ExportarRelatorio.calcular_data_sete_dias_antes(data_entrada)
        
        resultado_filtragem = {
            "informacoes":[
                {
                    'id': value.id,
                    'data_entrada': value.data_entrada,
                    'data_saida': value.data_saida,
                    'hora_entrada': value.hora_entrada,
                    'hora_saida': value.hora_saida
                } for value in query_informacoes
            ]
        }
        return resultado_filtragem