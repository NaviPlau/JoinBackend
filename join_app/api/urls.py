from django.urls import path
from .views import ContactListCreateView, ContactDetailView, TaskViewSet

urlpatterns = [
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list-create'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='task-detail'),
]