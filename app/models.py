from .import db
from datetime import datetime as dt

class Stock(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    company_name = db.Column(db.String)
    company_ticker =db.Column(db.String)
    date_created = db.Column(db.DateTime, default=dt.utcnow)


def __repr__(self):
    return f"<Stock: [{self.company_name}] {self.company_ticker} >"


def save(self):
    db.session.add(self)
    db.session.commit()


def delete(self):
    db.ession.remove(self)
    db.session.commit

