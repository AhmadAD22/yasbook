from provider_details.models import Store,CommonQuestion
from django import forms

from django import forms

class StoreSpecialistForm(forms.ModelForm):
    class Meta:
        model = CommonQuestion
        fields = ( 'question', 'answer')
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})    
        }