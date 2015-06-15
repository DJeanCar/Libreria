from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30,
					widget = forms.TextInput(attrs = {
							'type' : 'text',
							'class' : 'custom_class',
							'placeholder' : 'Username'
						})
				)
	password = forms.CharField(max_length=30,
					widget = forms.TextInput(attrs = {
							'type' : 'password',
							'class' : 'custom_class',
							'placeholder' : 'Password'
						})
				)

	def clean(self):
		if not User.objects.filter(username = self.cleaned_data['username']).exists():
			self.add_error('username', 'El nombre de usuario no existe!!')
		else:
			user = User.objects.get(username = self.cleaned_data['username'])
			if not user.check_password(self.cleaned_data['password']):
				self.add_error('password', 'El password es incorrecto')