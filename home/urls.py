from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserTaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),  # This includes the tasks/ route
    path('user/<int:user_id>/tasks/', UserTaskViewSet.as_view({'get': 'list'}), name='user-tasks'),
]