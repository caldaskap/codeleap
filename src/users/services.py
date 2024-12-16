from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .repositories import UserRepository

class UserService:
    @staticmethod
    def register_user(validated_data):
        username = validated_data.get('username')
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')
        email = validated_data.get('email')

        if password != password_confirm:
            raise ValidationError({"password": "Passwords must match."})

        if UserRepository.username_exists(username):
            raise ValidationError({"username": "A user with that username already exists."})

        if UserRepository.user_exists_by_email(email):
            raise ValidationError({"email": "This email is already in use."})

        user = UserRepository.create_user(password=password, **validated_data)
        refresh = RefreshToken.for_user(user)

        return {
            'user': validated_data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @staticmethod
    def login_user(validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = UserRepository.authenticate_user(username, password)
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            raise ValidationError("Invalid credentials or inactive user.")
