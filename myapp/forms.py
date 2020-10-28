from django import forms

class FeebackForm(forms.Form):
    title = forms.CharField(label = 'Title',max_length=50,widget=forms.TextInput)
    subject=forms.CharField(label = 'Subject Description',max_length=200,widget=forms.Textarea)