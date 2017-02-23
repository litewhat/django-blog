from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_email(self):
        email = self.data['email']
        qs = User.objects.filter(email__exact=email)
        if qs.count() != 0:
            raise forms.ValidationError('This email address is already used.')
        return email

    def clean_password(self):
        password = self.data['password']
        validate_password(password)
        return password

    def clean_confirm_password(self):
        password = self.data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password should match.')
        return confirm_password