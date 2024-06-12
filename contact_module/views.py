from django.shortcuts import render
from django.views import View
from .forms import ContactUsModelForm


# Create your views here.
class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'contact_module/contact_us_page.html', {
            'contact_form': contact_form
        })

    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, 'contact_module/home_page.html')
        return render(request, 'contact_module/contact_us_page.html', {
            'contact_form': contact_form
        })
