from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.forms import inlineformset_factory
from .models import TwitchUser, Bang
from .utils import auth
import datetime


def login_view(request):
    if request.user.is_authenticated:
        print("AUTHENTICATED")
        return bangs(request)

    if "code" in request.GET:
        # Get info from request necessary to make token request
        code = request.GET["code"]
        scope = request.GET["scope"]

        # Call auth function to get new auth info
        auth_dict = auth.token_request(code)
        expiration_date = datetime.datetime.now() + datetime.timedelta(
            seconds=int(auth_dict["expires_in"])
        )

        # Call auth function to get user info with the token provided by twitch
        user_dict = auth.get_user_dict(auth_dict["access_token"])

        try:
            # If the user exists, update it's auth info.
            twitch_user = TwitchUser.objects.get(twitch_id=int(user_dict["id"]))
            user = User.objects.get(username=twitch_user.twitch_id)
            twitch_user.access_token, twitch_user.refresh_token, twitch_user.expiration_date, twitch_user.scope = (
                auth_dict["access_token"],
                auth_dict["refresh_token"],
                expiration_date,
                auth_dict["scope"],
            )
            user.set_password(twitch_user.access_token)
            user.save()
            twitch_user.save()

            # Authenticate
            user = authenticate(
                username=twitch_user.twitch_id, password=twitch_user.access_token
            )
            print(
                "User {} UPDATED! New token: {}".format(
                    twitch_user.twitch_name, twitch_user.access_token
                )
            )
        except TwitchUser.DoesNotExist:
            # If user doesn't exist, create new one with parameters given by auth and user info.
            user = User.objects.create_user(
                username=user_dict["id"],
                email=user_dict["email"],
                password=auth_dict["access_token"],
            )
            twitch_user = TwitchUser(
                twitch_id=int(user_dict["id"]),
                twitch_name=user_dict["display_name"],
                email=user_dict["email"],
                access_token=auth_dict["access_token"],
                refresh_token=auth_dict["refresh_token"],
                expiration_date=expiration_date,
                scope=scope,
                user=user,
            )
            twitch_user.save()
            user = authenticate(
                username=user_dict["id"], password=auth_dict["access_token"]
            )
            print("User {} CREATED".format(twitch_user.twitch_name))
            login(request, user)
            return bangs(request)

        # Log in User and render bangs
        if user is not None:
            login(request, user)
            print("User LOGED IN")
        return bangs(request)

    else:
        # If this request doesn't have 'code', we request it and render the view again to further process 'code'
        get_request = auth.authorize_request(
            "chat:read+chat:edit+openid+user:read:email"
        )
        context = {"get_request": get_request}

    return render(request, "bangs/login.html", context)


@login_required(login_url="/bot/login/")
def bangs(request):
    user = request.user
    BangInlineFormset = inlineformset_factory(
        User, Bang, fields=("command", "response"), extra=1
    )
    if request.method == "POST":
        bang_formset = BangInlineFormset(request.POST, request.FILES, instance=user)
        if bang_formset.is_valid():
            bang_formset.save()
    bang_formset = BangInlineFormset(instance=user)
    for form in bang_formset:
        for field in form:
            if field.name == "DELETE":
                field.field.widget.attrs.update({'class': 'form-check-input'})
                continue
            field.field.widget.attrs.update({'class': 'form-control'})
    return render(request, "bangs/bangs.html", {"bang_formset": bang_formset})


def home(request):
    get_request = auth.authorize_request(
        "chat:read+chat:edit+openid+user:read:email"
    )
    context = {"get_request": get_request}
    return render(request, "bangs/index.html", context)
