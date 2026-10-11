from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Enables "Log in" button in the browser

    # Include all API routes from tasks app (auth endpoints & /tasks/)
    path('', include('tasks.urls')),
]
