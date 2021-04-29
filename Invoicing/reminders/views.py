from django.shortcuts import render, redirect
from .forms import *
from .models import Texts
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView



def listOfTexts(request):
    """
    Returning a list of all the texts reminders created
    """
    text = Texts.objects.all()
    
    context = {
        'texts': text,
    }
    return render(request, 'reminders/list_reminders.html', context)


class CreateServ(View):
    """
    Create  New Services for a specific user
    """
    
    form_class = TextReminder
    initial = {'key': 'value'}
    template_name = 'reminders/creating_reminders.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            
            clt = form.save(commit=False)
            clt.owner = request.user
            clt.save()
            return redirect('reminders:createReminders')
        else:
            print('noooooooooooooo')
        return render(request, self.template_name, context=context)


class TextUpdate(UpdateView):
    """
    Update reminder's texts
    """
    model = Texts
    template_name = 'reminders/update.html'
    context_object_name = 'text'
    fields = ('text',)
    def get_success_url(self):
        return reverse_lazy('reminders:listReminders')