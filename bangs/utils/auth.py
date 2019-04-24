import os
import requests
import json

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET_ID = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8000/bot/login'
# REDIRECT_URI = 'http://127.0.0.1:8000/burritobot_app/login/'


def authorize_request(scope):
    print(CLIENT_ID, CLIENT_SECRET_ID)
    request = 'https://id.twitch.tv/oauth2/authorize?response_type=code&client_id={}&redirect_uri={}&scope={}'.format(CLIENT_ID,REDIRECT_URI,scope)
    return request


def token_request(code):
    url = 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&code={}&grant_type=authorization_code&redirect_uri={}'.format(CLIENT_ID, CLIENT_SECRET_ID, code, REDIRECT_URI)
    request = requests.post(url)
    response_dict = json.loads(request.text)
    print(response_dict)
    return response_dict


def get_user_dict(token):
    url = 'https://api.twitch.tv/helix/users?scope=user:read:email'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(url, headers=headers).json()['data'][0]
    return response

def refresh_token(token):
    url = 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=refresh_token&refresh_token={}'.format(CLIENT_ID, CLIENT_SECRET_ID, token)
    response = requests.post(url)
    if response.status_code == requests.codes.ok:
        return response.json()
