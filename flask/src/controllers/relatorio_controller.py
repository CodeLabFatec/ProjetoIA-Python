from log import logging

from flask import request, jsonify
from flask_api import status


from models.services.exportar_relatorio import ExportarRelatorio

class RelatorioController:

    def download_relatorio_7_dias():
        return ExportarRelatorio.export_relatorio_7_dias('Template7dias.xlsx')
    
    def download_relatorio_14_dias():
        return ExportarRelatorio.export_relatorio_14_dias('Template14dias.xlsx')
    
    def download_relatorio_14_dias():
        return ExportarRelatorio.export_relatorio_14_dias('Template14dias.xlsx')

    def download_redzone_log_excel_all():
        return ExportarRelatorio.generate_redzone_log_excel_all()

    def download_redzone_log_excel(id):
        return ExportarRelatorio.generate_redzone_log_excel(id)
    
    def download_relatorio_7_dias_por_id(id):
        return ExportarRelatorio.export_relatorio_por_id('Template7dias.xlsx', id)