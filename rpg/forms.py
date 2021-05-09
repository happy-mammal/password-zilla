from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,HTML


class SignUpForm(UserCreationForm):
		first_name = forms.CharField(label="First Name", max_length=30)
		last_name = forms.CharField(label="Last Name", max_length=30)
		class Meta:
				model = User
				fields = ['username', 'email', 'password1', 'password2']



class GeneratorForm(forms.Form):

		len_choices=()
		for x in range (1,21):
			len_choice = (x,x)
			len_choices+=(len_choice,)

		password_length = forms.ChoiceField(label="Password Length", choices=len_choices)

		has_chars = forms.BooleanField(label="Inclue letters",required = False)
		has_digits = forms.BooleanField(label="Inclue digits",required = False)
		has_symbols = forms.BooleanField(label="Inclue symbols",required = False)

		case_choices=[('upper','Upper Case'),('lower','Lower Case'),('mixed','Mixed Case')]

		password_case = forms.ChoiceField(label="Password Case", choices=case_choices)

		occurence_choices=[(True,'Unique'),
         (False,'Repeated')]

		occurence = forms.ChoiceField(choices=occurence_choices, widget=forms.RadioSelect)

		result_choices=()
		for x in range (1,11):
			result_choice = (x,x)
			result_choices+=(result_choice,)

		results_no = forms.ChoiceField(label="Number of Results", choices=result_choices)

		preset_title = 	forms.CharField(label="Preset Title",max_length=30)


	



		
		
		
		