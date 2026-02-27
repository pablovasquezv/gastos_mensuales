from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'tipo', 'color']
        
        # Personalizamos los widgets para agregar clases de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Alimentación, Salario, Transporte...',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control form-control-color w-100',
                'type': 'color', # Esto activa el selector de color nativo del navegador
                'title': 'Elige un color para identificar esta categoría'
            }),
        }
        
        labels = {
            'nombre': 'Nombre de la Categoría',
            'tipo': 'Tipo de Transacción',
            'color': 'Color Distintivo',
        }

    # Opcional: Validación personalizada
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre.capitalize()