from . import db
from datetime import datetime
class listnote(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    notes = db.Column(db.String(1000), default="")

    timestamp = db.Column(db.DateTime, default=0, nullable=False)

    def __init__(self, notes: str):
        self.notes = notes
        self.timestamp = datetime.now()


def get_note_by_id(id:int) -> listnote:

    return listnote.query.filter_by(id=id).first()

def get_all_note() -> listnote:
    return listnote.query.order_by(listnote.id.desc()).all()
    
