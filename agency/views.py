from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import PortfolioItem1

def contact_view(request):
    # Fetch all portfolio items from the database
    portfolio_items = PortfolioItem1.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject=f"New contact from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Return a success message (no redirect, just render the same page with success feedback)
            success_message = "Form submission successful!"
            return render(request, 'agency/contact.html', {'form': form, 'portfolio_items': portfolio_items, 'success_message': success_message})

    else:
        form = ContactForm()

    # Return the contact form along with the portfolio items
    return render(request, 'agency/contact.html', {'form': form, 'portfolio_items': portfolio_items})

