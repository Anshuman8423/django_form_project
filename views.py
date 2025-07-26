from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Normally, save to DB or send email
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'formapp/contact_form.html', {'form': form})

def success_page(request):
    return render(request, 'formapp/success.html')
