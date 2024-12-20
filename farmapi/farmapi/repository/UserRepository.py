from farmapi import db, bcrypt
from farmapi.helpers import UserHelper
from farmapi.models import User, Role
from farmapi.mappers import map_userhelper_to_user, map_user_to_userhelper
class UserRepository:
    @staticmethod
    def create_user(userHelper:UserHelper):
        user = map_userhelper_to_user(userHelper)
        user.roles = []
        for role_name in userHelper.roles:
                role = Role.query.filter_by(slug=role_name).first()
                if role:
                    user.roles.append(role)
                else:
                    return f"Role '{role_name}' does not exist."
        db.session.add(user)
        db.session.commit()
        
        return map_user_to_userhelper(user)
    
    @staticmethod
    def getUserFromUsername(userHelper:UserHelper):
        user = map_userhelper_to_user(userHelper)
        user = User.query.filter_by(username=user.username).first()
        return user if user else None
    
    @staticmethod
    def getUserFromEmail(userHelper:UserHelper):
        user = map_userhelper_to_user(userHelper)
        user = User.query.filter_by(email=user.email).first()
        return user if user else None
    