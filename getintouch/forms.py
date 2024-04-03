from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    PROJECT_TYPES = (
        ('web_design', 'Web Design'),
        ('mobile_app', 'Mobile App'),
        ('graphic_design', 'Graphic Design'),
        ('other', 'Other'),
    )
    project_type = forms.ChoiceField(
        choices=PROJECT_TYPES,
        widget=forms.Select(attrs={'class': 'custom-dropdown', 'placeholder': 'Select project type'}),
        required=True  
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'city', 'project_type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name and surname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your City'}),
            'description': forms.Textarea(attrs={'placeholder': 'Short description of your project'}),
        }
