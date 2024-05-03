from app import db
from datetime import datetime

class SaidaRedZoneEntity(db.Model):

    __tablename__ = 'saida_redzone'
    __table_args__ = {'schema':'api_6sem'}

    id = db.Column(db.BigInteger, primary_key=True)
    data = db.Column(db.DateTime)
    id_redzone = db.Column(db.BigInteger, db.ForeignKey(
        "api_6sem.redzone.id"))