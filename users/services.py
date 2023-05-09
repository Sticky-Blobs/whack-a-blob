from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from web3.auto import w3

from .models import User


def user_login(address: str, signature: str, message: str):
    check_user = check_if_user_exists(address)

    if not check_user:
        new_user = create_user(address)
        address = new_user.address
        new_user.is_active = True
        new_user.save()

    authenticate_kwargs = {
        'address': address,
        'message': message,
        'signature': signature
    }

    user = authenticate(**authenticate_kwargs)

    if not user:
        raise ValidationError(
            'Incorrect login credentials'
        )
    tokens = RefreshToken.for_user(user)
    return {
        'access_token': str(tokens.access_token),
        'refresh_token': str(tokens),
    }


def check_if_user_exists(address: str):
    try:
        User.objects.get(address=address)
    except User.DoesNotExist:
        return False
    
    return True


def create_user(address: str):
    user = User.objects.create(address=address)
    
    return user
