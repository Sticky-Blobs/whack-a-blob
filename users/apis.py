from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from drf_yasg.utils import swagger_auto_schema

from .services import user_login


class LoginAPI(APIView):
    """
    Metamask Login

    Endpoint for handling wallet login
    """
    permission_classes = (permissions.AllowAny,)

    class InputSerializer(serializers.Serializer):
        address = serializers.CharField()
        signature = serializers.CharField()
        message = serializers.CharField()

        class Meta:
            ref_name = 'login input'

    class RefreshTokenSerializer(serializers.Serializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @swagger_auto_schema(
        request_body=InputSerializer,
        responses={200: RefreshTokenSerializer}
        )
    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            result = user_login(**input_serializer.validated_data)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(result, status=status.HTTP_200_OK)
