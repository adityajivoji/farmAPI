from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:adminaccess@localhost:5432/farmer_db'
app.config['SECRET_KEY'] = 'd58f5cf962eee2061'
app.config['JWT_SECRET_KEY'] = 'df8e5a7462e5c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
jwt = JWTManager(app)
blacklist = set()



from farmapi.routes.farmerRoutes import *
from farmapi.routes.farmRoutes import *
from farmapi.routes.scheduleRoutes import *
from farmapi.routes.view_routes import *
from farmapi.routes.userLogin import *
from farmapi.routes.userRegistration import *


with app.app_context():
    db.create_all()
    from farmapi.models import User
    super_user = User.query.filter_by(username="superadmin").first()
    if super_user:
        db.session.delete(super_user)
        db.session.commit()
    print("creating super admin")
    db.session.add(User(username="superadmin", password=bcrypt.generate_password_hash("superpassword").decode("utf-8"), role="superadmin", email="super@admin.com"))
    db.session.commit()
    print("created database, superadmin password", "superpassword")