from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
# Create your views here.


class APIpage(View):
    """ Displays API call"""
    def get(self, request):
        template = loader.get_template('pageViewer/index.html')
        """ API CALL """
        return HttpResponse(template.render({}, request))
