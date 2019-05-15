from rest_framework import viewsets
from rest_framework import serializers

from .models import TwitchUser, Bang


class TwitchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchUser
        fields = ('id', 'twitch_id', 'twitch_name', 'email', 'access_token')


class TwitchUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TwitchUserSerializer
    queryset = TwitchUser.objects.all()


class BangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bang
        fields = ('command', 'response', 'user')


class BangViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BangSerializer
    queryset = Bang.objects.all()
