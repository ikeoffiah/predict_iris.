from django import forms



class PredForms(forms.Form):
    sepal_length = forms.FloatField(required=True)
    sepal_width = forms.FloatField(required=True)
    petal_length = forms.FloatField(required=True)
    petal_width = forms.FloatField(required=True)



