from farmapi.models import User
from farmapi.helpers import UserHelper
from farmapi import bcrypt

def map_userhelper_to_user(user_helper: UserHelper) -> User:
    return User(
        username=user_helper.username,
        password=bcrypt.generate_password_hash(user_helper.password).decode('utf-8'), 
        email=user_helper.email,
        role=user_helper.roles
    )


def map_user_to_userhelper(user: User) -> UserHelper:
    return UserHelper(
        id=user.id,
        username=user.username,
        email=user.email,
        roles=user.role,
        password="hidden"
    )
