from django.forms import ModelForm

from .models import Profile
from bootstrap_plugin import simpleFactory

class ProfileForm(simpleFactory(ModelForm)):
    class Meta:
        model = Profile
        fields = ('email',)
