from django import forms


class EmailForm(forms.Form):
    First_Name = forms.CharField(label='First_Name', max_length=50)
    Last_Name = forms.CharField(label='Last_Name', max_length=50)
    Email = forms.EmailField(label='Email', max_length=100)
    Telephone = forms.IntegerField(label='Telephone')
    Company = forms.CharField(label='Company', max_length=100)
    Description = forms.CharField(label='Description', max_length=1000)

