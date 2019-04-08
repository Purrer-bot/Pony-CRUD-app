from django import forms

from .models import Horse, Owner, Genotype, Lab, Color

class PostForm(forms.ModelForm):

    class Meta:
        model = Horse
        fields = ('horse_name', 'sex', 'birth_date', 'horse_color', 'genes', 'owner', 'photo')

class OwnForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = ('name', 'phone', 'address', 'farm', 'country', 'email')

class GenForm(forms.ModelForm):
    class Meta:
        model = Genotype
        fields = ('base_formula', 'silver', 'cream', 'dun', 'champagne', 'disease', 'lab', 'color', 'description')

class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('lab_name', 'lab_country', 'lab_method', 'lab_date')

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ('base_color', 'white_color', 'marks')
