from django.forms import ModelForm
from geoportal.models import Comment, Post, GetFile


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class DocumentForm(ModelForm):
    class Meta:
        model = GetFile
        fields = ('title', 'file', )

