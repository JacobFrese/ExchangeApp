from django import forms
from toolExchange.models import tool
from django.forms.widgets import NumberInput

CATEGORIES= [
    ('------', '------'),
    ('Power Tool', 'Power Tool'),
    ('Hand Tool', 'Hand Tool'),
    ('Other', 'Other'),
    ]

class postForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":80}))
    category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))
    price = forms.IntegerField()
    class Meta():
        model = tool
        fields = ('title', 'description', 'category', 'price')

class requestForm(forms.Form):
    start_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    end_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
