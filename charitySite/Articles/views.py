from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
# Create your views here.


class Homepage(View):
    def get(self, request):
        template = loader.get_template('articles/index.html')  #  Templates folder needs to be within App is True
        return HttpResponse(template.render({"Key": 12}, request))
