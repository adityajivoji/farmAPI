from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required
from functools import wraps


def requires_roles(*roles):
    def wrapper(fn):
        @jwt_required()
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if "role" not in claims or claims["role"] not in roles:
                return jsonify(
                    {
                        "error": "You do not have necessary permission to access this resource"
                    }
                ), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper