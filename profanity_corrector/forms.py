from django import forms
from .models import UserResponse


class EnterText(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ("user_response",)
