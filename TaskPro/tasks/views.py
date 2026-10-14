from rest_framework import generics, viewsets, permissions
from django.shortcuts import render
from .models import Task
from .serializers import UserRegistrationSerializer, TaskSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status_param = self.request.query_params.get('status')
        if status_param and status_param.lower() != 'all':
            queryset = queryset.filter(status__iexact=status_param)

        priority_param = self.request.query_params.get('priority')
        if priority_param and priority_param.lower() != 'all':
            queryset = queryset.filter(priority__iexact=priority_param)

        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset.order_by('due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')
