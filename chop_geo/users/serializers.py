from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers, exceptions
from rest_framework.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from chop_geo.users.models import OTPCode

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "model_name"]

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    newpassword = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        exclude = ["is_staff", "groups", "user_permissions", "password"]
        extra_kwargs = {
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_superuser': {'read_only': True},
            'picture': {'read_only': True}
        }

    def update(self, instance, validated_data):
        new_password = validated_data.pop('newpassword', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance


class UserMeSerializer(serializers.Serializer):
    user = UserSerializer(many=False)


class UserEmailResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ConfirmOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()


class TokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    model_name = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    otp_code = serializers.CharField(max_length=6)

    default_error_messages = {
        "no_active_account": "No active account found with the given credentials"
    }

    token_class = RefreshToken

    def validate(self, attrs):
        username = attrs.get("username")
        name = attrs.get("name")
        model_name = attrs.get("model_name")
        otp_code = attrs.get('otp_code')

        user, _created = get_user_model().objects.get_or_create(
            username=username, defaults={"name": name, "model_name": model_name})

        # Validate OTP code
        # try:
        #     otp_record = OTPCode.objects.get(user=user, code=otp_code)
        # except OTPCode.DoesNotExist:
        #     raise exceptions.AuthenticationFailed(
        #         self.error_messages["invalid_otp"],
        #         "invalid_otp",
        #     )

        if otp_code != "1234":
            raise exceptions.AuthenticationFailed(
                {"invalid_otp": "invalid_otp", }
            )

        self.user = user
        refresh = self.get_token(self.user)
        data = {}
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)  # type: ignore
