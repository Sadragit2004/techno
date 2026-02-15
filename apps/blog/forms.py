from django import forms

class CommentForm(forms.Form):

    full_name = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class':'','placeholder':'نام کامل'}))
    email = forms.EmailField(max_length=100,label='',required=False,widget=forms.TextInput(attrs={'class':'','placeholder':'ایمیل'}))
    text = forms.CharField(max_length=1000,label='',widget=forms.Textarea(attrs={'class':'','placeholder':'پیام ...'}))