from sqladmin import ModelView
from models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.full_name, User.role]