from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer


# View for registering a new user
class RegisterView(APIView):
    # Allow anyone to access the register endpoint
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        # Check if incoming data is valid
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate JWT tokens for the newly created user
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'message': 'User registered successfully!',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        
        # Return error if validation failed
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ViewSet for handling CRUD operations on tasks
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    # Only authenticated users can access task endpoints
    permission_classes = [permissions.IsAuthenticated]

    # Get only tasks that belong to the logged-in user
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-id')

    # Automatically set the owner to the current logged-in user when creating a task
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
