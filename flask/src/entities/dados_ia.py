from app import db
from datetime import datetime, date, time

class informacoesEntity(db.Model):

    __tablename__ = 'redzone'
    __table_args__ = {'schema':'api_6sem'}

    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(1000), nullable=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Boolean)