from log import logging

from flask import request
from flask_api import status


from models.services.exportar_relatorio import ExportarRelatorio

class RelatorioController:

    def download_relatorio_7_dias():
        return ExportarRelatorio.export_relatorio_7_dias()
    
    def download_relatorio_14_dias():
        return ExportarRelatorio.export_relatorio_14_dias()
