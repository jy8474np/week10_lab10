from django import forms
from .models import Place 

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place 
        fields = ('name', 'visited')

class DateInput(forms.DateInput): # Created to provide ensure accurate date input in 'date_visited' field below
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes' , 'date_visited' , 'photo') # Fields to appear on HTML
        # Widget below will use DateInput class above to ensure entry is a valid date
        widgets = {
            'date_visited': DateInput() # 'date_visited' now will not just be a text field that will accept any text input
        }
