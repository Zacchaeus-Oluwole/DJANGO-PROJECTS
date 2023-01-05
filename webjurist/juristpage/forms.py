from django import forms
from .models import Perpetrator


class PerpetratorForm(forms.ModelForm):
    gender = forms.CharField(label="Gender: ", widget=forms.RadioSelect(choices=(('male','Male'),('female','Female'))), required=True)
    date = forms.CharField(widget=forms.SelectDateWidget)
    class Meta:
        model = Perpetrator
        fields = "__all__"