from app import db
from datetime import datetime

class EntradaRedZoneEntity(db.Model):

    __tablename__ = 'entrada_redzone'
    __table_args__ = {'schema':'api_6sem'}

    id = db.Column(db.BigInteger, primary_key=True)
    data = db.Column(db.DateTime)
    id_redzone = db.Column(db.BigInteger)