from django import forms
from .models import Booking
from .models import Contact


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name',
                                           'class': 'form-control',
                                           'data-msg': 'Please enter at least 4 chars',
                                           'data-rule': 'minlen:4',
                                           'id': 'name'
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'phone',
                                            'placeholder': 'Your Phone'}),
            'date_time': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'date',
                                                'placeholder': 'Date'}),
            'date': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'date',
                                           'placeholder': 'Date'}),
            'time': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'time',
                                           'placeholder': 'Time'}),
            'people': forms.NumberInput(attrs={'class': 'form-control',
                                               'id': 'people',
                                               'placeholder': '# of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'rows': '5',
                                             'placeholder': 'Message'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        model = Booking
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name',
                                           'class': 'form-control',
                                           'data-msg': 'Please enter at least 4 chars',
                                           'data-rule': 'minlen:4',
                                           'id': 'name'
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'phone',
                                            'placeholder': 'Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'rows': '5',
                                             'placeholder': 'Message'}),
        }



