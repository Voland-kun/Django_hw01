from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']



# class ProductForm(forms.Form):
#     id = forms.IntegerField(min_value=0)
#     name = forms.CharField(max_length=50)
#     description = forms.CharField(widget=forms.Textarea)
#     price = forms.DecimalField(min_value=0)
#     quantity = forms.IntegerField(min_value=0)
#     date = forms.DateTimeField
#     photo = forms.ImageField()
#
# def clean_name(self):
# """Плохой пример. Подмена параметра min_length."""
# name = self.cleaned_data['name']
# if len(name) < 3:
# raise forms.ValidationError('Имя должно содержать не
# менее 3 символов')
# return name
# def clean_email(self):
# email: str = self.cleaned_data['email']
# if not (email.endswith('vk.team') or
# email.endswith('corp.mail.ru')):
# raise forms.ValidationError('Используйте корпоративную
# почту')
# return email




# class ManyFieldsFormWidget(forms.Form):
# name = forms.CharField(max_length=50,
# widget=forms.TextInput(attrs={'class':
# 'form-control',
# 'placeholder': 'Введите имя пользователя'}))
# email =
# forms.EmailField(widget=forms.EmailInput(attrs={'class':
# 'form-control',
# 'placeholder': 'user@mail.ru'}))
# age = forms.IntegerField(min_value=18,
# widget=forms.NumberInput(attrs={'class': 'form-control'}))
# height =
# forms.FloatField(widget=forms.NumberInput(attrs={'class':
# 'form-control'}))
# is_active = forms.BooleanField(required=False,
# widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
# birthdate = forms.DateField(initial=datetime.date.today,
# widget=forms.DateInput(attrs={'class': 'form-control'}))
# gender = forms.ChoiceField(choices=[('M', 'Male'), ('F',
# 'Female')],
# widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
# message =
# forms.CharField(widget=forms.Textarea(attrs={'class':
# 'form-control'}))


# class ImageForm(forms.Form):
#     image = forms.ImageField()