from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer


# 1. Register a new user
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'User registered successfully!',
            'username': user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=201)

    return Response(serializer.errors, status=400)


# 2. List all tasks or create a new task
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list(request):
    # GET: return tasks owned by the logged-in user
    if request.method == 'GET':
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    # POST: create a new task for the logged-in user
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 3. Retrieve, update, or delete a single task by ID
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk, owner=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

    # GET: return task details
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # PUT: update task
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE: delete task
    elif request.method == 'DELETE':
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=204)
