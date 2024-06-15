from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review

RATING_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),)

class ProductForm(forms.ModelForm):
    """ A form for store admins to add products to the store """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Form class for users to review on a product 
    """

    rating = forms.ChoiceField(choices=RATING_CHOICES)

    class Meta:
        model = Review
        fields = ('content','rating')
