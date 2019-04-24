from rest_framework import viewsets
from rest_framework import serializers
from .models import TwitchUser


class TwitchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchUser
        fields = ('twitch_id', 'twitch_name', 'email')


class TwitchUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TwitchUserSerializer
    queryset = TwitchUser.objects.all()
