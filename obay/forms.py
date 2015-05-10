from django import forms
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, PrependedAppendedText, StrictButton
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from obay.models import Item, Bid, User, UserProfile

# TODO: save image to subdirectory for auction
class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = 'add_item'
        self.helper.form_class = 'col-md-9 col-md-offset-1'
        #self.helper.label_class = 'col-sm-2'
        #self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            Fieldset(
                'Item information',
                'name',
                'description',
                'donor',
                'pic',
                'category'
                ),
            FormActions(
                Submit('submit', 'Submit'),
                Button('cancel', 'Cancel', onclick='history.go(-1);')
                )
            )
        self.fields['description'].widget.attrs['rows'] = 4
    
    class Meta:
        model = Item
        fields = ('name', 'description', 'donor', 'pic', 'category')

class BidForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        self.item = kwargs.pop('item', None)
        super(BidForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('item', kwargs={'item_name_slug': self.item.slug}) 
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedAppendedText('amount', '$', '.00'),
            Submit('submit', 'Bid', css_class='btn-primary')
            )


    class Meta:
        model = Bid
        fields = ('amount',)

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        topbid = self.item.top_bid()
        if topbid and (amount <= topbid.amount):
            raise ValidationError("Bid needs to be higher than the current top bid of ${}".format(topbid.amount))

        return amount

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('club', 'isteam')

