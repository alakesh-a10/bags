from django import forms
class BagsForm(forms.Form):
    Feedback=forms.CharField(widget=forms.TextInput)






