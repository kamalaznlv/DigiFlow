from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')
