from django import forms
from obay.models import Item, Bid, User, UserProfile

class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    description = forms.CharField()
    pic = forms.ImageField()
    category = forms.ChoiceField(choices=Item.CATEGORY_CHOICES)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Item
        fields = ('name', 'description', 'pic', 'category')

# TODO: add to is_valid to see if bid is higher than previous bid!
class BidForm(forms.ModelForm):
    #Item
    amount = forms.IntegerField()

    class Meta:
        model = Bid
        fields = ('amount',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('club', 'isteam')