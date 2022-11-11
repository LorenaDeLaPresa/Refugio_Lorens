from django import forms
from blog.models import Adopcion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = [
              'usuario',
              'animal',
              'razones',
             
        ]
        labels = {
            'usuario':'Adoptante',
            'animal':'Animal',
            'razones': 'Razones para adoptar',
        }
        widgets = {            
            
            'razones':forms.Textarea(attrs={'class':'form-control'}),

        }
        