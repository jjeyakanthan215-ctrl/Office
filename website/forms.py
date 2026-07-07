from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Your Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Your Email Address',
                'required': 'required'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Subject (Optional)'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input form-textarea', 
                'placeholder': 'How can we help build your future?',
                'rows': 5,
                'required': 'required'
            }),
        }
