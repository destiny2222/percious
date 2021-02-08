from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)



    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)    

