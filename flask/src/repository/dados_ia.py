from models.dto.informacoes import informacoesDTO
from entities.dados_ia import informacoesEntity
from entities.entrada_redzone import EntradaRedZoneEntity
from entities.saida_redzone import SaidaRedZoneEntity


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
            informacoesEntity.data_cadastro,
            informacoesEntity.status,
            EntradaRedZoneEntity.data
        ).join(
            informacoesEntity, informacoesEntity.id == EntradaRedZoneEntity.id_redzone
        ).filter(
            EntradaRedZoneEntity.data >= data_sete_dias_atras
        ).order_by(
            EntradaRedZoneEntity.data
        )

        resultado_filtragem = [
        {
            'data_entrada': value.data.strftime("%Y-%m-%d")
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
    
        print(contagem_pessoas['datas'].values())
        return list(contagem_pessoas['datas'].values())
    

    def get_redzone_entries(id):

        query = db.session.query(
            EntradaRedZoneEntity.data.label("data_entrada"),
            SaidaRedZoneEntity.data.label("data_saida"),
            informacoesEntity.id
        ).join(
            informacoesEntity, informacoesEntity.id == EntradaRedZoneEntity.id_redzone
        ).outerjoin(
            SaidaRedZoneEntity, SaidaRedZoneEntity.id_redzone == informacoesEntity.id
        ).filter(
            informacoesEntity.id == id
        ).order_by(
            EntradaRedZoneEntity.data
        )

        resultado_filtragem = [
        {
            'data_entrada': value.data_entrada.strftime("%Y-%m-%d"),
            'data_saida': value.data_saida.strftime("%Y-%m-%d")
        } for value in query
    ]
        return resultado_filtragem