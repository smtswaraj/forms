from django import forms
from . models import Review

# class reviewForm(forms.Form):
#     username = forms.CharField(max_length=20,error_messages={
#         'required':'Username cannot be Empty',
#         'max_length':'Username should be less than 20'
#         })
#     feedback = forms.CharField(widget = forms.Textarea())

class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"                    #['user_name','feedback']
        labels = {
            'user_name':'Your Name',
            'feedback':'Your Review'
        }
        error_messages = {
            'user_name':{'required':'Username cannot be empty'}
        }