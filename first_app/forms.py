from django import forms
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_COLORS_CHOICES1 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_COLORS_CHOICES2 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_COLORS_CHOICES3 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class TestForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Please enter your email address",)
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    first_name = forms.CharField(initial='Your name')
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES1)
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES2)
    favorite_color4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES3,)
    


