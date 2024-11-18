from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")

        for character in username:
            if character not in string.ascii_lowercase:
                raise UserInputError("Username must only contain letters a-z")

        if password != password_confirmation:
            raise UserInputError("Password and password confirmation are different")

        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        only_letters = True
        for character in password:
            if character not in string.ascii_letters:
                only_letters = False
        if only_letters:
            raise UserInputError("Password cannot contain only letters")


user_service = UserService()
