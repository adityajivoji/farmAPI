from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:adminaccess@localhost:5432/farmer_db'
app.config['SECRET_KEY'] = 'd58f5cf962eee2061'
app.config['JWT_SECRET_KEY'] = 'df8e5a7462e5c'
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
jwt = JWTManager(app)
blacklist = set()



from farmapi.routers.farmerRoutes import farmer_bp
from farmapi.routers.farmRoutes import farm_bp
from farmapi.routers.scheduleRoutes import schedule_bp
from farmapi.routers.userLogin import userlogin_bp
from farmapi.routers.userRegistration import userregister_bp
from farmapi.routers.view_routes import views_bp
from farmapi.routers.TestRoutes import test_routes_bp

app.register_blueprint(farmer_bp)
app.register_blueprint(farm_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(userlogin_bp)
app.register_blueprint(userregister_bp)
app.register_blueprint(views_bp)
app.register_blueprint(test_routes_bp)



with app.app_context():
    db.create_all()
    from farmapi.utils import initialize_roles_and_superadmin
    initialize_roles_and_superadmin(db)