from django.shortcuts import render
# from django.views.generic import TemplateView
from .forms import EmailForm
from django.core.mail import send_mail


# class HomeView(TemplateView):
#     template_name = 'main.html'


def email(request):
    if request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('First_Name')
            last_name = form.cleaned_data.get('Last_Name')
            email = form.cleaned_data.get('Email')
            telephone = form.cleaned_data.get('Telephone')
            telephone = str(telephone)
            company = form.cleaned_data.get('Company')
            description = form.cleaned_data.get('Description')

            send_mail(
                'Chat',
                'Name: ' + first_name + ' ' + last_name + '\n'
                + 'Email: ' + email + '\n'
                + 'Telephone: ' + telephone + '\n'
                + 'Company: ' + company + '\n'
                + 'Description: ' + description,
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
    return render(request, 'main.html')





