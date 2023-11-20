from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if username.isalpha() == False:
            raise AuthenticationError("Username must be only letters a-z")

        if self._user_repository.find_by_username(username) == False:
            raise AuthenticationError("Username is taken")

        if len(username) < 3:
            raise AuthenticationError("Username must be atleast 3 letters long")

        if len(password) < 8:
            raise AuthenticationError("Password must be atleast 8 characters long")

        if password.isalpha():
            raise AuthenticationError("Password must not have only letters")
