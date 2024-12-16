from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def user_exists_by_email(email):
        return User.objects.filter(email=email).exists()

    @staticmethod
    def username_exists(username):
        return User.objects.filter(username=username).exists()

    @staticmethod
    def create_user(**validated_data):
        return User.objects.create_user(**validated_data)

    @staticmethod
    def authenticate_user(username, password):
        return authenticate(username=username, password=password)
