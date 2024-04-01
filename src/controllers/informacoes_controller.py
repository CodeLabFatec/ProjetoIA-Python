from flask import request
from flask_api import status

from repository.dados_ia import informacoesRepository
from entities.dados_ia import informacoesEntity
from log import logging
from app import db

class informacoesController:

    def listar():
        response = informacoesRepository.get_all()
        logging.info("Sucesso no Listar")
        return response
    
    def salvar():
        try:
            body = request.get_json()
            informacoes = informacoesEntity(
                horario_entrada = body["horario_entrada"],
                horario_saida = body["horario_saida"]
            )

            informacoesRepository.save(informacoes)
            logging.info("Sucesso no Salvar")
            db.session.commit()
            return {'id':informacoes.id}, status.HTTP_200_OK
        except Exception as erro:
            logging.exception("Erro no Salvar")
            db.session.rollback()
            return {'Info':'Erro Interno'}, status.HTTP_500_INTERNAL_SERVER_ERROR