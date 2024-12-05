from farmapi import app, db, bcrypt
from flask import request
from farmapi.models import User
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles

@app.route("/register/admin", methods=['POST'])
@jwt_required()
@requires_roles("superadmin")
def register_admin():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not username or not password:
        return "missing username or password"
    if User.query.filter_by(username=username).first():
        return "message", "username already in use, choose different or login"
    if User.query.filter_by(email=email).first():
        return "message", "email already in use"
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(
        username = username,
        password = hashed_password,
        email = email,
        role = "admin"
    )

    db.session.add(user)
    db.session.commit()

    return "Admin Added Successfully"

@app.route("/register/superadmin", methods=['POST'])
@jwt_required()
@requires_roles("superadmin")
def register_superadmin():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not username or not password:
        return "missing username or password"
    if User.query.filter_by(username=username).first():
        return "message", "username already in use, choose different or login"
    if User.query.filter_by(email=email).first():
        return "message", "email already in use"
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(
        username = username,
        password = hashed_password,
        email = email,
        role = "superadmin"
    )

    db.session.add(user)
    db.session.commit()

    return "Super Admin Added Successfully"


@app.route("/register/user", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def register_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not username or not password:
        return "missing username or password"
    if User.query.filter_by(username=username).first():
        return "message", "username already in use, choose different or login"
    if User.query.filter_by(email=email).first():
        return "message", "email already in use"
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(
        username = username,
        password = hashed_password,
        email = email,
        role = "user"
    )

    db.session.add(user)
    db.session.commit()

    return "User Added Added Successfully"