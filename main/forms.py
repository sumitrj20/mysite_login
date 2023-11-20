from django import forms 
from .models import details 


class detail_emp(forms.ModelForm):

    class Meta:
        model=details
        fields='__all__'
