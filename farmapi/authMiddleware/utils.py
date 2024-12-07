from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required, get_current_user
from functools import wraps


def requires_roles(*roles):
    def wrapper(fn):
        @jwt_required()
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if "roles" not in claims:
                return jsonify({"msg": "Roles are missing from the token"}), 403
            user_roles_list = claims["roles"]
            if not any(role in user_roles_list for role in roles):
                return jsonify({"msg": "User does not have necessary permission to access this resource"})
            return fn(*args, **kwargs)
        return decorator
    return wrapper