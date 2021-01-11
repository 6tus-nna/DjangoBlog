from django import forms
from . models import Post, Category, Comment, Reply

choice = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choice:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','author','header_image', 'category', 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
           #'author' : forms.Select(attrs={'class':'form-control','value':'', 'id':'user'}),
            'author' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),


        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control'}),
            


        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields =('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control'}),
            


        }
    


class EditpostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
            

        
