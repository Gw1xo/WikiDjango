from django import forms

class CreateArticleForm(forms.Form):
    name = forms.CharField(label="Name:")
    markdown = forms.Textarea()
    