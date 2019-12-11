from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
# Create your views here.


class Homepage(View):
    def get(self, request):
        template = loader.get_template('charities/index.html')  #  Templates folder needs to be within App is True
        print("Hitting the charity home page")
        return HttpResponse(template.render({"cssFile": 'articles/index.css'}, request))

    def post(self, request, *args, **kwargs):
        """ Triggered when a form has been posted within the funds.html"""
        template = loader.get_template('Charities/templates/charities/index.html')
        return HttpResponse(template.render({"cssFile": 'articles/index.css'}, request))
