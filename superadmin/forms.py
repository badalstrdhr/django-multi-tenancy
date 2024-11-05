from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'raw_password', 'cu_role')

    def clean_raw_password(self):
        raw_password = self.cleaned_data.get('raw_password')
        if not raw_password:
            raise forms.ValidationError("This field cannot be empty.")
        return raw_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['raw_password'])  
        user.raw_password = self.cleaned_data['raw_password'] 
        if commit:
            user.save()
        return user