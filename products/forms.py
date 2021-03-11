from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    # Defines form and fields wanted to be included
    class Meta:
        model = Product
        fields = '__all__'

        # to override the __init__ to make some changes to the fields
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            # create a list of tuples of the friendly names associated with their category ids
            # syntax = list comprehension, short hand way of adding items to a list
            friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

            # update caegory field to use friendly name for choices instead of ID
            self.fields['category'].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'


