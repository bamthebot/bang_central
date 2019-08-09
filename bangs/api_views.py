from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import serializers

from .models import TwitchUser, Bang


class TwitchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchUser
        fields = ('twitch_id', 'twitch_name', 'email', 'access_token', 'user')


class TwitchUserViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = TwitchUserSerializer
    queryset = TwitchUser.objects.all()


class BangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bang
        fields = ('command', 'response', 'user')


class BangViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = BangSerializer
    queryset = Bang.objects.all()
