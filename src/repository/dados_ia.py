from models.dto.informacoes import informacoesDTO
from entities.dados_ia import informacoesEntity

from app import db
from datetime import *

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

    def get_informacoes_for_export():

        data_atual = datetime.now()
        data_sete_dias_atras = data_atual - timedelta(days=7)

        query_informacoes = db.session.query(
            informacoesEntity.id,
            informacoesEntity.data_entrada,
            informacoesEntity.data_saida,
            informacoesEntity.hora_entrada,
            informacoesEntity.hora_saida
        ).filter(
            informacoesEntity.data_entrada >= data_sete_dias_atras
        ).order_by(
            informacoesEntity.data_entrada
        )

        resultado_filtragem = [
                {
                    'data_entrada': value.data_entrada.strftime("%Y-%m-%d")
                } for value in query_informacoes
            ]

        return resultado_filtragem
    
    def calcula_entrada_pessoas():
        
        datas_filtradas = informacoesRepository.get_informacoes_for_export()
        contagem_pessoas = {'datas':{}}

        for data in datas_filtradas:
            if data['data_entrada'] not in contagem_pessoas['datas']:
                contagem_pessoas['datas'][data['data_entrada']] = {'numero_pessoas' : 0, 'data_entrada' : data['data_entrada']}
            contagem_pessoas['datas'][data['data_entrada']]['numero_pessoas'] += 1

        return list(contagem_pessoas['datas'].values())