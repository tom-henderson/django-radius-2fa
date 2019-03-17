from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms

import pyotp


class Token(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    secret = models.CharField(default=pyotp.random_base32, max_length=16) # TODO Encrypt the secret


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ('user',)


class TokenAdmin(admin.ModelAdmin):
    form = TokenForm

admin.site.register(Token, TokenAdmin)