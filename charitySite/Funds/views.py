from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import wikiPagesModel
# Create your views here.
from .appUpdate import updateApp


class Homepage(View):
    """ Displays a scroll view with all the possible funds, request for an API before loading screen"""
    def get(self, request):
        #  updateApp()  # Only use this function if you want to refresh the App with new Articles
        template = loader.get_template('articles/funds.html')  #  Templates folder needs to be within App is True
        return HttpResponse(template.render({}, request))

    def post(self, request, *args, **kwargs):
        titleOne = wikiPagesModel.objects.get(id=1)
        context = {
                'Oceans': titleOne.fundOneURL,
                'Hunger': titleOne.fundTwoURL,
                'Trees': titleOne.fundThreeURL,
                'Globalwarming': titleOne.fundFourURL
        }
        template = loader.get_template('articles/funds.html')
        return HttpResponse(template.render(context, request))


class InfoPage(View):
    """ Displays an Info View """
    def post(self, request, *args, **kwargs):
        title = request.POST['title']  # GETS THE TITLE OF PAGE
        template = loader.get_template('info/index.html')
        return HttpResponse(template.render({'title': title}, request))


class NewsPage(View):
    """ Displays an News View """
    def post(self, request, *args, **kwargs):
        title = request.POST['title']  # GETS THE TITLE OF PAGE
        template = loader.get_template('news/index.html')
        return HttpResponse(template.render({'title': title}, request))


class SettingsPage(View):
    """ Displays an Settings View """
    def post(self, request, *args, **kwargs):
        title = request.POST['title']  # GETS THE TITLE OF PAGE
        template = loader.get_template('settings/index.html')
        return HttpResponse(template.render({'title': title}, request))


class Charitypage(View):

    def post(self, request, *args, **kwargs):
        """ This will be used to set title of page and request for API """
        title = request.POST['title']
        field_object = wikiPagesModel._meta.get_field(request.POST['fund'])
        field_value = field_object.value_from_object(wikiPagesModel.objects.get(id=1))
        template = loader.get_template('charity/index.html')
        return HttpResponse(template.render({'title': title, 'words': field_value}, request))
