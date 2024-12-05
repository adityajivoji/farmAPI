
from datetime import datetime
from farmapi import db

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(25), nullable=False)
    crop_grown = db.Column(db.String(25), nullable=False)
    sowing_date = db.Column(db.DateTime,  nullable=True, default=None)
    village = db.Column(db.String(25), nullable = False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    schedule = db.relationship('Schedule', backref = 'farm', lazy= True)
    
    
    def __repr__(self):
        return f"Farm_{self.id}('{self.area}', '{self.crop_grown}', '{self.village}')"

    