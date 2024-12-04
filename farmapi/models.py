
from datetime import datetime
from farmapi import db, app


class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    language = db.Column(db.String(25), nullable=False)
    farm = db.relationship('Farm', backref = 'owner', lazy=True)

    def __repr__(self):
        return f"Farmer_{self.id}('{self.name}', '{self.language}', '{self.phone}')"

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(25), nullable=False)
    crop_grown = db.Column(db.String(25), nullable=False)
    sowing_date = db.Column(db.DateTime, default=datetime(1990, 1, 1))
    village = db.Column(db.String(25), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    schedule = db.relationship('Schedule', backref = 'farm', lazy= True)
    def __repr__(self):
        return f"Farm_{self.id}('{self.area}', '{self.crop_grown}', '{self.village}')"

    

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    days_after_sowing = db.Column(db.Integer, nullable=False)
    fertilizer = db.Column(db.String(25), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    quantity_unit = db.Column(db.String(5), nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)

    def __repr__(self):
        return f"Farm_{self.id}('{self.days_after_sowing}', '{self.fertilizer}', '{self.quantity}{self.quantity_unit}')"

with app.app_context():
    db.create_all()
    print("created database")