from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import CustomForm


def custom(request):

    if request.method == 'POST':
        custom_form = CustomForm(request.POST)
        if custom_form.is_valid():
            name = custom_form.cleaned_data['name']
            email = custom_form.cleaned_data['email']
            message = custom_form.cleaned_data['message']

            body = render_to_string(
                'custom/confirmation/body.txt',
                {'message': message, 'email': email, 'name': name})

            send_mail(
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('custom'))
        else:
            messages.error(request, 'Oops! Something went wrong with your form!')
    else:
        custom_form = CustomForm()

    context = {
        'custom_form': custom_form,
    }
    template = 'custom/custom.html'
    return render(request, template, context)