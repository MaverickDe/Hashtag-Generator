

# from socket import fromshare
from email.mime import image
from django import forms
from base.models import Image


class Saveimgform(forms.ModelForm):
    class Meta:
        model= Image
        fields = "__all__"
