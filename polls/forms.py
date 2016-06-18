from django.forms import ModelForm
from polls.models import Choice, Poll
from django.contrib.auth.models import User


# Create the form class.
class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['dob']       
        labels = {'dob': 'podaj datę '}
        
class UpdateChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['dob']
        labels = {'dob': 'zmień datę '}
        

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ['username']
        labels = {'username': 'Podaj nazwę użytkownika '}

