from flask import Blueprint
from controllers.informacoes_controller import InformacoesController
from controllers.relatorio_controller import RelatorioController

infos_bp = Blueprint('infos_bp', __name__)
infos_bp.route('/info/listar',
               methods=['GET'])(InformacoesController.listar)
infos_bp.route('/info',
               methods=['POST'])(InformacoesController.salvar)


relatorio_bp = Blueprint('relatorio_bp', __name__)
relatorio_bp.route('/report',
               methods=['POST'])(RelatorioController.download_relatorio)
