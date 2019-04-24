from django.core.management.base import BaseCommand, CommandError
from bangs.models import TwitchUser
from bangs.utils.auth import refresh_token


def handle(self, *args, **kwargs):
    try:
        bot_user = TwitchUser.objects.get(email="dowy.vz6@gmail.com")
    except TwitchUser.DoesNotExist:
        print("Bot user does not exist")
        return
    refresh_data = refresh_token(bot_user.refresh_token)
    if 'status' in refresh_data.keys():
        if refresh_data['status'] == 400:
            print('Couldn\'t refresh token.')
            return
    bot_user.access_token = refresh_data['access_token']
    bot_user.refresh_token = refresh_data['refresh_token']
    bot_user.save()
    print('Token refreshed succesfully!')

