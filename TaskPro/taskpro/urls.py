from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import RegisterView, TaskViewSet, login_page, register_page, dashboard_page

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('dashboard/')),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
