from django import forms
from .models import Insurance, User, Coverage

class InsuranceForm(forms.ModelForm):
    
    class Meta:
        model = Insurance
        fields = ('name', 'insurance_class', 'price', 'urls')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'name', 'password')

class CoverageForm(forms.ModelForm):

    class Meta:
        model = Coverage
        fields = ('insuranceId', 'car', 'medicine', 'third_party', 'lost')