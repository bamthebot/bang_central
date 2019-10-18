from django.contrib.auth.models import User
from django.forms import inlineformset_factory, ModelForm
from .models import TwitchUser, Bang, Blast


BangInlineFormset = inlineformset_factory(
    User, Bang, fields=("command", "response"), extra=1
)


BlastInlineFormset = inlineformset_factory(
    TwitchUser, Blast, fields=("name", "value"), extra=1
)


class CommandPrefixForm(ModelForm):
    class Meta:
        model = TwitchUser
        fields = ["command_character"]


def set_form_styles(form):
    for field in form:
        if field.name == "DELETE":
            field.field.widget.attrs.update({"class": "form-check-input"})
            continue
        field.field.widget.attrs.update({'class': 'form-control'})


def set_formset_styles(formset):
    for form in formset:
        set_form_styles(form)


def get_user_formsets(request, user, twitch_user):
    bang_formset = BangInlineFormset(instance=user)
    blast_formset = BlastInlineFormset(instance=twitch_user)
    set_formset_styles(bang_formset)
    set_formset_styles(blast_formset)
    return {"bang_formset": bang_formset, "blast_formset": blast_formset}


def post_user_formsets(request, user, formset_type="bang"):
    twitch_user = TwitchUser.objects.get(user=user)
    if formset_type == "bang":
        formset = BangInlineFormset(request.POST, request.FILES, instance=user)
    elif formset_type == "blast":
        formset = BlastInlineFormset(request.POST, request.FILES, instance=twitch_user)
    if formset.is_valid():
        formset.save()
