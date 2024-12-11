from farmapi import bcrypt, loginManager, jwt, blacklist
from flask import Blueprint, request, jsonify
from farmapi.models import User
from flask_login import login_user, logout_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from farmapi.authMiddleware.utils import requires_roles


@loginManager.user_loader
def load_user(user_id): 
    return User.query.get(int(user_id))

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist

userlogin_bp = Blueprint('userlogin', __name__)


@userlogin_bp.route("/test", methods=['POST'])
def test():
    return jsonify({"msg": "I am responding"})

@userlogin_bp.route("/login", methods=['POST'])
def login():
    # TODO: Add current user logic
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return "missing username or password"
    user = User.query.filter_by(username=username).first()
    if not user:
        return "Username not present"
    user_roles = [role.slug for role in user.roles]
        
    if bcrypt.check_password_hash(user.password, password):
        jwt_token = create_access_token(
            identity = str(user.id),
            additional_claims = {
                "roles": user_roles
            }
        )
        login_user(user, remember=False)
        return jsonify(
            {
                "message": "Login Successful",
                "access_token":jwt_token
            }, 200
        )
    else:
        return "Incorrect Password"
    

@userlogin_bp.route("/logout", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def logout():
    jti = get_jwt()['jti']
    blacklist.add(jti)
    logout_user()
    return "Logged Out Successfully"
    

    

    
