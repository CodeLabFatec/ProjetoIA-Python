from app import db
from datetime import datetime

class informacoesEntity(db.Model):

    __tablename__ = 'informacoes'
    __table_args__ = {'schema':'teste'}

    id = db.Column(db.BigInteger, primary_key=True)
    horario_entrada = db.Column(db.DateTime, default=datetime.now)
    horario_saida = db.Column(db.DateTime, default=datetime.now)