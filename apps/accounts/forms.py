from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    # Definimos el email como obligatorio y profesional
    email = forms.EmailField(
        required=True, 
        label="Correo electrónico",
        help_text="Requerido. Se enviará un correo de verificación."
    )

    class Meta:
        model = User
        # 'password1' y 'password2' ya vienen integrados en UserCreationForm
        fields = ("username", "email") 
        labels = {
            'username': 'Nombre de usuario',
        }

    def __init__(self, *args, **kwargs):
        """
        Sobrescribimos el init para aplicar estilos Bootstrap a todos los campos
        sin repetir código (DRY: Don't Repeat Yourself).
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})

    def clean_email(self):
        """
        Validación extra: Evita que se registren dos usuarios con el mismo correo.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado. Intenta con otro.")
        return email