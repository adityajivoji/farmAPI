from farmapi.models import User, Role
from farmapi.helpers import UserHelper
from farmapi import bcrypt

def map_userhelper_to_user(user_helper: UserHelper) -> User:
    user = User(
        username=user_helper.username,
        password=bcrypt.generate_password_hash(user_helper.password).decode('utf-8'), 
        email=user_helper.email
    )
    for role in user_helper.roles:
        r = Role.query.filter_by(slug=role).first()
        user.roles.append(Role(name=r.name, slug=r.slug))
    return user


def map_user_to_userhelper(user: User) -> UserHelper:
    return UserHelper(
        id=user.id,
        username=user.username,
        email=user.email,
        roles=user.roles,
        password="hidden"
    )
