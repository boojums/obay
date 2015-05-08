from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions, PrependedAppendedText

from obay.models import Item, Bid, User, UserProfile

# TODO: save image to subdirectory
class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = 'add_item'
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
                Submit('submit', 'Add item')
                )
            )

    # name = forms.CharField(max_length=50)
    # description = forms.CharField()
    # donor = forms.CharField(max_length=128)
    # pic = forms.ImageField()
    # category = forms.ChoiceField(choices=Item.CATEGORY_CHOICES)
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # auction = forms.CharField(widget=forms.HiddenInput(), required=False)
    # contact = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Item
        fields = ('name', 'description', 'donor', 'pic', 'category')

class BidForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        self.item = kwargs.pop('item', None)
        super(BidForm, self).__init__(*args, **kwargs)

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