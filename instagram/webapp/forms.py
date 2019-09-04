from django import forms
from django.forms import widgets

from webapp.models import Post, Comment


class PostForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True
    )

    class Meta:
        model = Post
        fields = ['picture', 'description']


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        max_length=1000,
        widget=widgets.Textarea
    )

    class Meta:
        model = Comment
        fields = ['text']
