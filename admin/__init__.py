from sqladmin import Admin
from admin.views.user import UserAdmin

def create_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    return admin