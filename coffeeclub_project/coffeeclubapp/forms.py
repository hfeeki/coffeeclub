from django.forms.models import ModelForm
from .models import CoffeeOrder, Customer, CustomerPref

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs['class'] = 'autocomplete'
        self.fields['customer'].help_text="start typing to see available customers"
        self.fields['coffee_name'].widget.attrs['class'] = 'autocomplete'
        self.fields['coffee_name'].help_text="start typing to see available Menu Items"

    class Meta:
        model=CoffeeOrder

class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['groups'].widget.attrs['class'] = 'autocomplete'
        self.fields['groups'].label="Group"
        self.fields['groups'].help_text="start typing to see available groups"
    class Meta:
        model=Customer
        exclude=('language','user','user_permissions','reporting_location','preferences')
    def clean(self):
        cleaned_data = self.cleaned_data
        if self._errors and 'email' in self._errors:
            raise forms.ValidationError("Email already exists")
        else:
            return cleaned_data


class PrefrencesForm(ModelForm):
    class Meta:
        model=CustomerPref
