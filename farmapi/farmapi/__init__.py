from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from farmapi.config import Config

db = SQLAlchemy()
# migrate = Migrate(app, db)
bcrypt = Bcrypt()
loginManager = LoginManager()
jwt = JWTManager()
blacklist = set()
blacklist = set()


    
def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, supports_credentials=True, origins="https://farmapifront.web.app")


    print("App created")
    from farmapi.routers.farmerRoutes import farmer_bp
    from farmapi.routers.farmRoutes import farm_bp
    from farmapi.routers.scheduleRoutes import schedule_bp
    from farmapi.routers.userLogin import userlogin_bp
    from farmapi.routers.userRegistration import userregister_bp
    from farmapi.routers.view_routes import views_bp
    from farmapi.routers.TestRoutes import test_routes_bp
    print("Register Blueprints")
    app.register_blueprint(farmer_bp)
    app.register_blueprint(farm_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(userlogin_bp)
    app.register_blueprint(userregister_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(test_routes_bp)
    db.init_app(app)
    bcrypt.init_app(app)
    loginManager.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        db.create_all()
        from farmapi.utils import initialize_roles_and_superadmin
        initialize_roles_and_superadmin(db)
    print("App Creation Completed")
    return app