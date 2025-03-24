from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task, User
from .serializers import TaskSerializer, AssignTaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk=None):
        task = self.get_object()
        serializer = AssignTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Users assigned successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTaskViewSet(viewsets.ViewSet):
    def list(self, request, user_id=None):
        tasks = Task.objects.filter(assigned_users__id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
