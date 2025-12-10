from django import forms
from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # Ou os campos que você deseja exibir
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano de Fabricação',
            'model_year': 'Ano do Modelo',
            'serie': 'Série',
            'plate': 'Código',
            'value': 'Valor',
            'photo': 'Foto',
        }

    # Funções de validação sempre começam com "clean". Exemplo: validar o campo model, a função é def clean_model(sef)

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value <= 0:
            self.add_error('value', 'O valor não pode ser zero ou negativo.')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is None or factory_year < 1995:
            self.add_error(
                'factory_year', 'Não é possível cadastrar um brinquedo fabricado antes de 1995.')
        return factory_year
