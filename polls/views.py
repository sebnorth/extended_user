from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .models import Choice, Poll
import csv
from django.http import HttpResponse
from .forms import ChoiceForm, PollForm, UserForm, UpdateChoiceForm
from polls.templatetags import polls_helpers



def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    choices = range(len(Choice.objects.all()))
    for i, choice in zip(choices, Choice.objects.all()):
        writer.writerow([i, choice.user.username, str(choice.dob), polls_helpers.allowed(choice), choice.rumber, polls_helpers.BizzFuzzTag(choice.rumber)])
    return response

def delete_choice(request, pk):
    
    try:
       instance = Choice.objects.get(id=pk)
    except Choice.DoesNotExist:
        instance = None
    if not instance:
        return HttpResponseRedirect('/polls')
    
    pom=instance.user
    try:
        instance.delete()    
    except polls.models.DoesNotExist:
        pass  
    try:
        pom.delete()    
    except polls.models.DoesNotExist:
        pass  
    
    return HttpResponseRedirect('/polls')

def create_choice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST)
        choice_form = ChoiceForm(request.POST)
        # check whether it's valid:
        if user_form.is_valid() and choice_form.is_valid():
            dob = choice_form.cleaned_data['dob']
            new_choice = Choice.objects.create(dob=dob)
            username = user_form.cleaned_data['username']
            new_user = User.objects.create_user(username=username,
                                 email='jlennon@beatles.com',
                                 password='glass onion')
            new_user.save()
            new_choice.user=new_user
            new_choice.age=new_choice.howold()
            new_choice.save()
            return HttpResponseRedirect('/polls')

    # if a GET (or any other method) we'll create a blank form
    else:
        user_form = UserForm()
        choice_form = ChoiceForm()

    return render(request, 'polls/forms.html',  {'user_form': user_form, 'choice_form': choice_form})

def update_choice(request, pk):
    # if this is a POST request we need to process the form data   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        choice_form = UpdateChoiceForm(request.POST)
        # check whether it's valid:
        if choice_form.is_valid():
            choice_instance = Choice.objects.get(id=pk)
            dob = choice_form.cleaned_data['dob']
            choice_instance.dob = dob
            choice_instance.age=choice_instance.howold()
            choice_instance.save()
            return HttpResponseRedirect('/polls')

    # if a GET (or any other method) we'll create a blank form
    else:
        choice_instance = Choice.objects.get(id=pk)
        choice_form = UpdateChoiceForm(instance=choice_instance)

    return render(request, 'polls/forms.html',  {'choice_form': choice_form})
    
class IndexView(generic.ListView):
    model = Choice
    template_name = 'polls/index.html'
    context_object_name = 'lista_c'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Choice.objects.all()


class ChoiceDetailView(generic.DetailView):
    model = Choice
    template_name = 'polls/detail.html'
    context_object_name = 'c'
        
    def get_context_data(self, **kwargs):
        context = super(ChoiceDetailView, self).get_context_data(**kwargs)
        return context

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

