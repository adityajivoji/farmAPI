from farmapi import db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    days_after_sowing = db.Column(db.Integer, nullable=False)
    fertilizer = db.Column(db.String(25), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    quantity_unit = db.Column(db.String(5), nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)

    def __repr__(self):
        return f"Farm_{self.id}('{self.days_after_sowing}', '{self.fertilizer}', '{self.quantity}{self.quantity_unit}')"