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
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return Response(data=users_serializer.data)
    elif request.method == 'POST':
        print(request.data)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)

        return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user_detail_view(request, pk=None):
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    elif request.method == 'PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(instance=user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)

        return Response(user_serializer.errors)

    elif request.method == 'DELETE':
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response({'mensaje': 'Eliminado'})
