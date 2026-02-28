from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        # Excluimos 'user' porque lo asignaremos en la vista (request.user)
        fields = ['categoria', 'descripcion', 'monto', 'fecha']
        
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-select select2-custom',
                'data-placeholder': 'Seleccione una categoría...'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Pago de arriendo, Compra de víveres...',
                'autocomplete': 'off'
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'form-control fw-bold text-primary',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'fecha': forms.DateInput(
                format='%Y-%m-%d', # <--- Esto es la clave
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
                ),
        }
        
        labels = {
            'categoria': 'Categoría del Gasto',
            'descripcion': 'Concepto',
            'monto': 'Importe ($)',
            'fecha': 'Fecha de Pago',
        }

    # Validación Pro: Asegurar que el monto sea siempre positivo
    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if monto <= 0:
            raise forms.ValidationError("El monto debe ser un valor mayor a cero.")
        return monto