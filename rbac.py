class Validation(object):
    def validate_data_in_db(self):
        pass


class RBAC(Validation):
    """ RBAC
        A role based auth system. System should be able to assign a role to a user and remove a role from a user.

        Entities are USER, ACTION TYPE, RESOURCE, ROLE

        ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)

        Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.

        Please list down the assumptions made."""

    ACTION_TYPE = {
        1: "READ",
        2: "WRITE",
        3: "DELETE"
    }

    RESOURCE = ["USER", "USER_ADDRESS", "USER_TRANSACTIONS", "RESOURCE", "ROLE"]
    # kind of parent child relation ship for hiraricle role
    ROLE = {"ADMIN": "ADMIN", "SUB_ADMIN": "ADMIN"}
    # PERMISSION = {role:{resourse_name:actions }}
    PERMISSION = {
        "ADMIN": {"USER": [1, 2], "USER_ADDRESS": [1, 2, 3], "ROLE": [1, 2, 3]},
        "SUB_ADMIN": {"USER_ADDRESS": [1, 2]}
    }

    BASE_DATA = {
        "users": {
            "pawan": {
                "UserId": "pawan01",
                "UserName": "pawan",
                "password": "pawan",
                "Role": ["ADMIN"]
            },

            "pawan01": {
                "UserId": "pawan01",
                "UserName": "pawan",
                "password": "pawan",
                "Role": ["SUB_ADMIN"]
            },
        },
        "Actions": {
            "USER": ["ADMIN", "SUB_ADMIN"],
            "USER_TRANSACTIONS": ["ADMIN", "SUB_ADMIN"]
        }
    }

    def __init__(self):
        super(RBAC, self).__init__()
        self.storage_unit()
        self.loggedin_user = "pawan"

    def storage_unit(self):
        self.database = self.BASE_DATA

    def add_role(self, role_name, parent_role):
        if role_name.get(role_name):
            print(f"Can not add this role {role_name}  its Duplicate")
            return
        elif parent_role and self.ROLE.get(parent_role):
            print(f"Not found role {role_name} in db")
            return

        self.ROLE[role_name] = role_name

    def add_user(self, user_data):
        if self.database.get("users").get(user_data.get("username")):
            print(f"please try diffrent username {user_data.get('username')}  its Duplicate")

        self.database.get("users")[user_data.get("usernmae")] = user_data
        print("User Added Sucessfully")

    def user_details(self, username):
        return self.database.get("users").get(username, {})

    def authenticate_user(self, username, password):
        user_data = self.database.get("users").get(username)
        if user_data:
            return user_data.get("password") == password
        return False

    def controle_unit(self):
        """
        for interating with console
        """

        pass

    def intials(self):
        print(f"""hi! you are logged in as admin {self.loggedin_user}
        press 1 for login as another user
        press 2 for create user
        press 3 for edit role""")
        input_val = int(input("Please Choose Options"))
        print(self.database)
        if input_val == 1:
            username = input("username  :")
            password = input("password :")
            if self.authenticate_user(username, password):
                self.loggedin_user = username
                print(f"LoggedIn As a {username}")
            else:
                print("username or password is wrong")
                return self.intials()

        elif input_val == 2:
            username = input("username  :")
            password = input("password  :")
            role = input("role  :").split(",")
            user_data = {
                "usename": username,
                "password": password,
                "role": role
            }
            if self.user_details(user_data):
                print("Already User")
                return self.intials()
            else:
                self.add_user(user_data)

        elif input_val == 3:
            role_ = input("RoleName  :")
            parent_role = input("parent_role  :")
            if not self.add_role(role_name, parent_role):
                return self.intials()


if __name__ == "__main__" :
    rbac_obj = RBAC()
    rbac_obj.intials()
