from rest_framework import serializers

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True, label='Confirm password')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords must match.')
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)