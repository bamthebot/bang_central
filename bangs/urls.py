from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

# Register api urls
router = DefaultRouter()
router.register(r'twitch_users', api_views.TwitchUserViewSet, basename="twitch_user")

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('bangs/', views.bangs, name='bangs'),
    path('api/', include((router.urls, 'bangs-api'))),
    path('', views.login_view, name='login'),
]

