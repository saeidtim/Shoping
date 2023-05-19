from django.forms import ModelForm, ValidationError
from django import forms
from .models import Comment

class CommentForm(ModelForm):
    def clean(self):
        n = self.changed_data['user']
        if n != 'mom':
            raise ValidationError('fosh dadi azizam')
        else:
            return n
    class Meta:
        model = Comment
        fields = ('text', )
