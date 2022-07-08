from django import forms

from .models import Quiz

class addQuestionForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'