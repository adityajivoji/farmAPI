from farmapi import db, bcrypt
from farmapi.helpers import UserHelper
from farmapi.models import User
from farmapi.mappers import map_userhelper_to_user, map_user_to_userhelper
class UserRepository:
    @staticmethod
    def create_user(userHelper:UserHelper):
        user = map_userhelper_to_user(userHelper)
        db.session.add(user)
        db.session.commit()
        
        return "User Added Successfully"
    
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
    