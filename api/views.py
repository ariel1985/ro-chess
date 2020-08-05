from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer, ChessGameSerializer
# from api.serializers import *
from chess_engine.models import *

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



class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows game to be viewed or edited.
    """
    queryset = GamePersistentData.objects.all()
    serializer_class = ChessGameSerializer
    permission_classes = [permissions.IsAuthenticated]
    
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