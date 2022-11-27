from django.forms import ModelForm
from app.models import Carros

# Create the form class.
class carrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']

