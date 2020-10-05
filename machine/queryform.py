from django import forms
#customer's information
class QueryForm(forms.Form):
    your_name=forms.CharField(label='Your name',max_length=100)
    your_email=forms.EmailField(label='Your email',max_length=100)
    subject=forms.CharField(label='Subject',max_length=100,required=False)
    message=forms.CharField(label='Message',widget=forms.Textarea,max_length=500,required=False)