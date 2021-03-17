from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TaskSerializer
from .models import Task


class TaskAllGenericView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TaskGenericView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user.id)
