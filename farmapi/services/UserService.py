from farmapi.repository import UserRepository
from farmapi.helpers.UserHelper import UserHelper

def validateUsernameAndPassword(userHelper):
    if not userHelper.username or not userHelper.password:
        return False
    if UserRepository.getUserFromUsername(userHelper):
        return False
    if UserRepository.getUserFromEmail(userHelper):
        return False
    return True

class UserService:

    @staticmethod
    def create_admin(username, password, email, roles):
        userHelper = UserHelper(username=username, password=password, email=email, roles=roles)
        if validateUsernameAndPassword(userHelper):
        
            return UserRepository.create_user(userHelper)
        else:
            return "Could not validate username and email"
    
    @staticmethod
    def create_superadmin(username, password, email, roles):
        userHelper = UserHelper(username=username, password=password, email=email, roles=roles)
        if validateUsernameAndPassword(userHelper):
        
            return UserRepository.create_user(userHelper)
        else:
            return "Could not validate username and email"
    
    @staticmethod
    def create_user(username, password, email, roles):
        userHelper = UserHelper(username=username, password=password, email=email, roles=roles)
        if validateUsernameAndPassword(userHelper):
        
            return UserRepository.create_user(userHelper)
        else:
            return "Could not validate username and email"
        
    