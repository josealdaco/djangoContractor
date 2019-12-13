from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
import requests
# Create your views here.


class APIpage(View):
    """ Displays API call"""
    def get(self, request):
        template = loader.get_template('pageViewer/index.html')
        """ API CALL """
        response = requests.get('https://charitywebsite.herokuapp.com/api/pages/?format=json')
        data = response.json()
        context = {
            'oceanTitle': data['fundOneTitle'],
            'oceanword':  data['fundOneURL'],
            'treeTitle': data['fundTwoTitle'],
            'treeword': data['fundTwoURL'],
            'hungerTitle': data['fundThreeTitle'],
            'hungerword': data['fundThreeURL'],
            'globalwarmingTitle': data['fundFourTitle'],
            'globalwarmingword': data['fundFourURL']
        }
        return HttpResponse(template.render(context, request))
