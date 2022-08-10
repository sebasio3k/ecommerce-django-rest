from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.serializers import UserSerializer
from apps.users.models import User


# Class based APIView:
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serialized = UserSerializer(users, many=True)
        return Response(data=users_serialized.data)


# Function based APIView:
@api_view(['GET', 'POST'])
def user_api_view(request):
    # List
    if request.method == 'GET':
        # Queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return Response(data=users_serializer.data, status=status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {
                    'mensaje': 'Usuario creado exitosamente!',
                    'data': user_serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user_detail_view(request, pk=None):
    # Queryset
    user = User.objects.filter(id=pk).first()

    # validation
    if user:

        # Retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(instance=user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)

            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'mensaje': 'Usuario eliminado'}, status=status.HTTP_200_OK)

    return Response({'mensaje': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
