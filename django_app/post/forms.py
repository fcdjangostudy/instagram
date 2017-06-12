from django import forms


class PostCreate(forms.Form):
    photo = forms.ImageField()


class PostModify(forms.Form):
    photo = forms.ImageField()
