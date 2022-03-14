
from multiprocessing.sharedctypes import Value


class NormalUser:
    def __init__(self, username) -> None:
        self.username = username
    
    @property
    def permission(self):
        return 460


class AdminUser:
    def __init__(self, username) -> None:
        self.username = username

    @property
    def permission(self):
        return 777


def authorize_users_factory(username: str, role: str):
    if role == "admin":
        return AdminUser(username)
    elif role == "user":
        return NormalUser(username)
    else:
        raise ValueError(f"Unknown user role {role}")
    

def login_user(username: str, password: str):
    try:
        user = None
        if username in data:
            user = data[username]
            if user["password"] == password:
                account = authorize_users_factory(username, user["role"])
                print(f"Username: {account.username} - Permossion: {account.permission}")
                return account
        else:
            raise Exception("Username or password is incorrect")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    data = {
        "adam": {
            "password": "123456",
            "role": "admin" 
        },
        "evan": {
            "password": "123456",
            "role": "user" 
        },
        "hacker": {
            "password": "123456",
            "role": "hacker" 
        },
    }
    try:
        login_user("adam", "123456")
        login_user("evan", "123456")
        login_user("hacker", "123456")
        login_user("adam2", "123456")
    except Exception as e:
        print(str(e))
