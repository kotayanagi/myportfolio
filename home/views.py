from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm
from .models import Work

def work(request):
    works = Work.objects
    return render(request, 'home.html', {'works': works})


'''
class ContactView(FormView):
   form_class = ContactForm

    def contact(self, request):
        form_class = ContactForm
        return render(request, 'contact.html', {'form': form_class})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
'''

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ['kyana875@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
