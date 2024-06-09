from django import forms

class contactform(forms.Form):
  nombre = forms.CharField(
    max_length=64,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  email = forms.EmailField(
    max_length=64,
    label='Correo Electrónico',
    widget=forms.EmailInput(attrs={'class': 'form-control'})
  )
  mensaje = forms.CharField(
    required=False,
    widget=forms.Textarea(attrs={'class': 'form-control', 'rows':4})
  )