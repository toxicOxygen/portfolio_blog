from django import forms

class SharePostForm(forms.Form):
    receipient_email = forms.EmailField()
    sender_email = forms.EmailField()
    sender_name = forms.CharField(max_length=25)
    comments = forms.CharField(required=False,widget=forms.Textarea)


