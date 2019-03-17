from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms

import pyotp


class Token(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    secret = models.CharField(default=pyotp.random_base32, max_length=16) # TODO Encrypt the secret

    @property
    def qr(self):
        return pyotp.totp.TOTP(self.secret).provisioning_uri(
            self.user.email,
            issuer_name="Django" # TODO should be site name / app setting?
        )


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ('user',)


class TokenAdmin(admin.ModelAdmin):
    form = TokenForm

admin.site.register(Token, TokenAdmin)