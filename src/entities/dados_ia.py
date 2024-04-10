from app import db
from datetime import datetime, date, time

class informacoesEntity(db.Model):

    __tablename__ = 'registros'
    __table_args__ = {'schema':'api_6sem'}

    id = db.Column(db.BigInteger, primary_key=True)
    data_entrada = db.Column(db.Date)
    hora_entrada = db.Column(db.Time)
    data_saida = db.Column(db.Date)
    hora_saida = db.Column(db.Time)