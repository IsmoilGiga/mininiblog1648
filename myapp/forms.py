from django import forms
from .models import Comment, Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Sarlavhani kiriting',
                'style': 'border-radius: 8px; padding: 10px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Tavsifni kiriting',
                'rows': 5,
                'style': 'border-radius: 8px; padding: 10px;'
            }),
            'image_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rasm URL manzilini kiriting',
                'style': 'border-radius: 8px; padding: 10px;'
            })
        }