from django import forms
from detail.models import ReviewBarang

class reviewform(forms.ModelForm):
    class Meta:
        model = ReviewBarang
        fields = {"comment"}