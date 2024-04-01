from flask import Blueprint
from controllers.informacoes_controller import informacoesController

infos_bp = Blueprint('infos_bp', __name__)
infos_bp.route('/info/listar',
               methods=['GET'])(informacoesController.listar)
infos_bp.route('/info',
               methods=['POST'])(informacoesController.salvar)