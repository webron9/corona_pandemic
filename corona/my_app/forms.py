from django import forms
from django.contrib.auth import get_user_model
from my_app.models import Profile,Donation
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class CustomProfileForm(UserCreationForm):
    location = forms.CharField(max_length=264)
    class Meta:
        model = User
        fields = ('username','password1','password2')
       
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['location'].label = 'Location'
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None

#modified code
class UserDonateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('item','amount')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['item'].label = 'Item'
        self.fields['amount'].label = 'Amount'
        
        