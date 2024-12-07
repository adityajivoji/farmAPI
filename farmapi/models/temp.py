from farmapi import db
from flask_login import UserMixin  

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Custom table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    roles = db.relationship("Role", secondary="userrole", back_populates='users')
    
    def has_role(self, role_slug):
        return any(role.slug == role_slug for role in self.roles)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}', {self.roles})"

class Role(db.Model):
    __tablename__ = 'roles'  # Custom table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship("User", secondary="userrole", back_populates="roles")
    
    def __repr__(self):
        return f"Role('{self.name}', '{self.slug}')"

userrole = db.Table('userrole',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),  # Adjust to match 'users'
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)  # Adjust to match 'roles'
)
