from rest_framework import viewsets, generics, filters
from user.models import User, Event
from user.serializer import UserSerializer, EventSerializer, ListEventsByUserIdSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    """Exibindo todos os users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

#    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'email']


class EventViewSet(viewsets.ModelViewSet):
    """Exibindo todos os events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

#    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]


class ListEventsByUserId(generics.ListAPIView):
    """Listando os events pelo ID do User"""

    def get_queryset(self):
        queryset = Event.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListEventsByUserIdSerializer

#    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]
