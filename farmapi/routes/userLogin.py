from farmapi import app,  bcrypt, loginManager, jwt, blacklist
from flask import request, jsonify
from farmapi.models import User
from flask_login import login_user, current_user, logout_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from farmapi.authMiddleware.utils import requires_roles
@loginManager.user_loader
def load_user(user_id): 
    return User.query.get(int(user_id))

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist


@app.route("/login", methods=['POST'])
def login():
    # TODO: Add current user logic
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return "missing username or password"
    user = User.query.filter_by(username=username).first()
    if not user:
        return "Username not present"
    if bcrypt.check_password_hash(user.password, password):
        jwt_token = create_access_token(
            identity = str(user.id),
            additional_claims = {
                "role": str(user.role)
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
    

@app.route("/logout", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def logout():
    jti = get_jwt()['jti']
    blacklist.add(jti)
    logout_user()
    return "Logged Out Successfully"
    

    

    
