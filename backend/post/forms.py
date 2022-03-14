from django import forms
from .models import Post, Tag, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'excerpt',
            'content',
            'image', 
            'category',
            'tag',
            'status',
            'comment_status',
        
        ]
        widgets = {
            'excerpt': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'tag': forms.CheckboxSelectMultiple(),
            'status': forms.RadioSelect(),
            'comment_status': forms.RadioSelect(),
        }