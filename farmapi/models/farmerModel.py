from farmapi import db

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    language = db.Column(db.String(25), nullable=False)
    farms = db.relationship('Farm', backref = 'owner', lazy=True)

    def __repr__(self):
        return f"Farmer_{self.id}('{self.name}', '{self.language}', '{self.phone}')"