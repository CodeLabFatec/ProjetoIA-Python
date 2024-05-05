from flask import Blueprint
from controllers.informacoes_controller import InformacoesController
from controllers.relatorio_controller import RelatorioController

infos_bp = Blueprint('infos_bp', __name__)
infos_bp.route('/info/listar',
               methods=['GET'])(InformacoesController.listar)
infos_bp.route('/info',
               methods=['POST'])(InformacoesController.salvar)


relatorio_bp = Blueprint('relatorio_bp', __name__)
relatorio_bp.route('/report-7-days',
               methods=['GET'])(RelatorioController.download_relatorio_7_dias)
relatorio_bp.route('/report-14-days',
               methods=['GET'])(RelatorioController.download_relatorio_14_dias)
relatorio_bp.route('/report-log',
               methods=['GET'])(RelatorioController.download_redzone_log_excel_all)
relatorio_bp.route('/report-log/<id>',
               methods=['GET'])(RelatorioController.download_redzone_log_excel)
relatorio_bp.route('/report-7-days/<id>',
               methods=['GET'])(RelatorioController.download_relatorio_7_dias_por_id)


def add_custom_headers(response):
    response.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
    return response