from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


class Homepage(View):
    def get(self, request):
        template = loader.get_template('articles/funds.html')  #  Templates folder needs to be within App is True
        return HttpResponse(template.render({"cssFile": 'articles/index.css'}, request))


class Charitypage(View):
    def get(self, request):
        print("Get for charity page recieved")
        template = loader.get_template('charity/index.html')
        return HttpResponse(template.render({'title': 'Ocean'}, request))
