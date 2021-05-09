from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from .models import Presets
from .generator import RandomPasswordGenerator

def home(request):
	return render(request, 'rpg/home.html', {"title": "Home"})

def about(request):
	return render(request, 'rpg/about.html', {"title": "About"})

@login_required
def generator(request):
	passwords = []
	if request.method== 'POST':
		
		form = forms.GeneratorForm(request.POST)
		
		if form.is_valid():
			
			if 'save' in request.POST:

				password_length = form.cleaned_data["password_length"]
				has_chars = form.cleaned_data["has_chars"]
				has_digits = form.cleaned_data["has_digits"]
				has_symbols = form.cleaned_data["has_symbols"]
				password_case = form.cleaned_data["password_case"]
				occurence = form.cleaned_data["occurence"]
				results_no = form.cleaned_data["results_no"]
				preset_title = 	form.cleaned_data["preset_title"]
								
				preset = Presets(
					user_id=request.user.id,
					p_length=password_length,
					is_letter=has_chars,
					is_digit=has_digits,
					is_symbol=has_symbols,
					p_case=password_case,
					is_unique=occurence,
					no_of_results=results_no,
					preset_title = preset_title,
					)

				preset.save()

				messages.success(request,f'Preset ({preset_title}) Saved Successfully!!')

				return redirect('rpg-generator')

			else:
				presets = Presets.objects.filter(user_id=request.user.id)
				rpg = RandomPasswordGenerator()

				password_length = int(form.cleaned_data["password_length"])
				has_chars = form.cleaned_data["has_chars"]
				has_digits = form.cleaned_data["has_digits"]
				has_symbols = form.cleaned_data["has_symbols"]
				password_case = form.cleaned_data["password_case"]
				occurence = bool(form.cleaned_data["occurence"])
				results_no = int(form.cleaned_data["results_no"])
				preset_title = 	form.cleaned_data["preset_title"]

				if(has_chars == False and has_digits == False, has_symbols == False):
					has_digits = True
					has_symbols = True

				passwords = rpg.onGeneratePressed(password_length,has_chars,has_digits,has_symbols,password_case,results_no,occurence)
				#passwords= [password_length,has_chars,has_digits,has_symbols,password_case,occurence,results_no]

	else:
		form = forms.GeneratorForm()	
		presets = Presets.objects.filter(user_id=request.user.id)
	
	return render(request, 'rpg/generator.html', {"title": "Generator","form":form,"presets":presets,"result":passwords})

def signin(request):
	return render(request, 'rpg/signin.html', {"title": "Sign In"})

def signup(request):
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			
			form.save()
			messages.success(request,f'Your account has been created {form.cleaned_data["username"]}! You are now able to login.')
			return redirect('rpg-signin')
	else:
		form = forms.SignUpForm()
	
	return render(request, 'rpg/signup.html', {"title": "Sign Up","form":form})


