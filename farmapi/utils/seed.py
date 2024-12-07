from farmapi.models import Role, User
from farmapi import bcrypt


def initialize_roles_and_superadmin(db):
    """Initialize roles and create a superadmin user if not already present."""
    roles = [
        {"name": "Super Admin", "slug": "superadmin"},
        {"name": "Admin", "slug": "admin"},
        {"name": "User", "slug": "user"},
    ]

    # Create or fetch roles
    created_roles = {}
    for role_data in roles:
        role = Role.query.filter_by(slug=role_data["slug"]).first()
        if not role:
            role = Role(name=role_data["name"], slug=role_data["slug"])
            db.session.add(role)
        created_roles[role_data["slug"]] = role

    db.session.commit()

    # Check if superadmin user exists
    super_user = User.query.filter_by(username="superadmin").first()
    if super_user:
        print("Superadmin user already exists. Skipping creation.")
    else:
        # Create superadmin user
        print("Creating superadmin user")
        super_user = User(
            username="superadmin",
            password=bcrypt.generate_password_hash("superpassword").decode("utf-8"),
            email="super@admin.com"
        )
        super_user.roles.append(created_roles["superadmin"])
        db.session.add(super_user)
        db.session.commit()
        print("Superadmin user created.")

    print("Roles and superadmin initialization completed.")