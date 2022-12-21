from django import forms

from driving_school.prices.models import CategoryPrice


class PricesBaseForm(forms.ModelForm):
    class Meta:
        model = CategoryPrice
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(
                attrs={
                    'placeholder': 'Category',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
            'description_practice': forms.Textarea(
                attrs={
                    'placeholder': 'Practise',
                }
            ),
            'description_theory': forms.Textarea(
                attrs={
                    'placeholder': 'Theory',
                }
            ),
            'description_test': forms.Textarea(
                attrs={
                    'placeholder': 'Test',
                }
            ),

            'description_not_included': forms.Textarea(
                attrs={
                    'placeholder': 'Not included',
                }
            ),
        }


class PricesCreateForm(PricesBaseForm):
    pass


