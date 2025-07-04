from model.entity.user import User
from model.besiness_logic.user_bl import UserBl


class UserController:
    def save(self, id, name, family, birth_date, user_name, password, role):
        try:
            user = User(id, name, family, birth_date, user_name, password, role)
            user.validate()
            user_bl = UserBl()
            user_bl.save(user)
            return "info: User saved successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def edit(self, name, family):
        try:
            user = User(name, family)
            user.validate()
            user_bl = UserBl()
            user_bl.edit(user)
            return "info: User edit successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def remove(self, id):
        try:
            user_bl = UserBl()
            user_bl.remove(id)
            return "info: User remove successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def find_by_name_and_family(self, name, family):
        pass

    def find_by_user_name(self, user_name):
        pass

    def find_by_role(self, role):
        pass
