from typing import Self
from django import forms


class CreateArticleForm(forms.Form):
    name = forms.CharField(label="Name:",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}
                           ))
    markdown = forms.CharField(label="Markdown:",
                               widget=forms.Textarea(
                                   attrs={'rows': '5', 'placeholder': 'Enter entry article', 'class': 'form-control'}
                               )
                               )