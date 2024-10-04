from rest_framework_simplejwt.tokens import RefreshToken

from ..api.serializer import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model, user_logged_out


#EndPoints

#registro de usuarios
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Obtener datos de usuario logueado
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Obtener a todos los usuarios registrados
class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Reescritura del tokenobtainpairview para disparar la señal
#y registrar el inicio de sesion
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Si la autenticación es exitosa, dispara la señal user_logged_in
        if response.status_code == status.HTTP_200_OK:
            user = self.get_user(request.data['username'])
            if user:
                print(f'Señal user_logged_in disparada para {user.username}')
                user_logged_in.send(sender=user.__class__, request=request, user=user)

        return response

    def get_user(self, username):
        User = get_user_model() #obteniendo modelo personalizado
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

#Logout para registro del fin de la conexion
class LogOutView(APIView):
    permission_classes = [IsAuthenticated]
    user = get_user_model()

    def post(self, request):
        try:
            #obteniendo e invalidando refreshtoken
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            #disparar la señal de logout para el registro
            user = request.user
            print(f'Señal user_logged_out disparada para {user.username}')
            user_logged_out.send(sender=user.__class__, request=request, user=user)
            return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)