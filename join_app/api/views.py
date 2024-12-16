from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Contact, Task
from .serializers import ContactSerializer, TaskSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound

class ContactListCreateView(APIView):
    def get(self, request):
        contacts = Contact.objects.filter(user=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
    

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally customize the queryset.
        For example, you can filter tasks based on the logged-in user.
        """
        return Task.objects.all()
    


    

    