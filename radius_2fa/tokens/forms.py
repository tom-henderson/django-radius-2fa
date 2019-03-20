from django import forms
from tokens.models import Token
from django.contrib.auth.forms import AuthenticationForm


class TokenAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    code = forms.CharField(max_length=6)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add bootstrap classes:
        for field in self.fields:
            checkbox_fields = [
                forms.CheckboxInput,
                forms.CheckboxSelectMultiple,
            ]
            if type(self.fields[field].widget) not in checkbox_fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
 
    def confirm_login_allowed(self, user):
        code = self.cleaned_data.get('code')

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            # User has no token.
            raise forms.ValidationError(
                "User has no token.",
                code='token_not_registered',
            )

        authenticated = token.verify(code)

        if not authenticated:
            # Invalid token.
            raise forms.ValidationError(
                "Token value incorrect.",
                code='invalid_token',
            )

        pass
