from django import forms
from .models import * 
from froala_editor.widgets import FroalaEditor




class TextReminder(forms.ModelForm):
    '''
    This form is for creating new reminders
    '''
    def __init__(self, *args, **kwargs):
        super(TextReminder, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control border-primary'})
    
    class Meta:
        model = Texts
        exclude = ['owner']