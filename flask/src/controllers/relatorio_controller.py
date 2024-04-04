from app import db
from log import logging

from flask import request
from flask_api import status


from models.services.exportar_relatorio import ExportarRelatorio

class RelatorioController:

    def download_relatorio():
        try:
            body = request.get_json()
            return ExportarRelatorio.export_relatorio(body['date_start'], body['date_end'])

        except Exception:
            logging.exception("Erro no Download")
            db.session.rollback()
            return {'Info':'Erro Interno'}, status.HTTP_500_INTERNAL_SERVER_ERROR