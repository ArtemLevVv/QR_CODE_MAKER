from django import forms

class Qrcode_Form(forms.Form):
    # Поле для посилання
    link = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Введіть посилання",
            'class': 'link'
        })
    )
    
    # Поле для кольору
    color = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'color',
            'placeholder': '#000000'
        }),
        label='Оберіть колір'
    )
    
    # Поле для розміру (якщо потрібен числовий введення, краще використовувати IntegerField або FloatField)
    size = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'id': 'slider',
            'min': '0',
            'max': '10000',
            'step': '50',
            'value': '100',
            'oninput': 'displayValue.value = slider.value',
        })
    )
