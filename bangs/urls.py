from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

# Register api urls
router = DefaultRouter()
router.register(r'twitch_users', api_views.TwitchUserViewSet, basename="twitch_user")
router.register(r'bangs', api_views.BangViewSet, basename="bangs")

urlpatterns = [
    path('bot/login/', views.login_view, name='login'),
    path('bot/bangs/', views.bangs, name='bangs'),
    path('bot/blasts/', views.blasts, name='blasts'),
    path('bot/prefix/', views.prefix, name='prefix'),
    path('bot/api/', include((router.urls, 'bangs-api'))),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
]
