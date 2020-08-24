from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.serializers import UserSerializer, GroupSerializer, UserSerializerWithToken  # , ChessGameSerializer
from chess_engine.models import *


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """
    
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class GameViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows game to be viewed or edited.
#     """
#     queryset = GamePersistentData.objects.all()
#     serializer_class = ChessGameSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#
# class RotemTestAPI(APIView):
#     """
#     View to list all users in the system.
#
#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     # authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         queryset = User.objects.all()
#         serializer_class = RotemSerializer
#         permission_classes = [permissions.IsAuthenticated]
#         content = 'rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR'
#         # usernames = [user.username for user in User.objects.all()]
#         return Response(content)
#