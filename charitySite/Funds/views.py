from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import wikiPagesModel
import requests
# Create your views here.
from .config import SECRET_KEY  #  Keeping my API Key a SECRET_KEY :)


class Homepage(View):
    """ Displays a scroll view with all the possible funds, request for an API before loading screen"""
    def get(self, request):
        title_list = ['Oceans', 'Hunger', 'Trees', 'Globalwarming']
        context = {}
        data_dict = {}
        for item in title_list:
            response2 = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&generator=search&inprop=url&gsrnamespace=0&gsrlimit=5&gsrsearch={}'.format(item))
            data = response2.json()['query']['pages']  #  Get list of pages
            first_key = list(data.keys())[0]  # Only want the first One
            article_url = data[first_key]['canonicalurl']  #  Only want the url
            context.update({item: article_url})
        #  Brute force way to create model, will optimize later

        data_dict.update({'fundOneURL': context.get(title_list[0]),
                          'fundTwoURL': context.get(title_list[1]),
                          'fundThreeURL': context.get(title_list[2]),
                          'fundFourURL': context.get(title_list[3])})
        m = wikiPagesModel(**data_dict)
        m.save()
        for objects in wikiPagesModel.objects.all():
            if objects.id != 1:
                wikiPagesModel.objects.get(id=objects.id).delete()
        template = loader.get_template('articles/funds.html')  #  Templates folder needs to be within App is True
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        titleOne = wikiPagesModel.objects.get(id=1)
        context = {
                'Oceans': titleOne.fundOneURL,
                'Hunger': titleOne.fundTwoURL,
                'Trees': titleOne.fundThreeURL,
                'Globalwarming': titleOne.fundFourURL
        }
        print(context)
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
        template = loader.get_template('charity/index.html')
        """ Starting to call API """
        diffbotparams = {'token': SECRET_KEY,
                         'url': request.POST['url'],
                         'paging': False,
                         'maxPages': 1,
                         'numPages': 1,
                         }
        response = requests.get('https://api.diffbot.com/v3/article?', diffbotparams)
        diffBot_Data = response.json()['objects'][0]['text']
        return HttpResponse(template.render({'title': title, 'words': diffBot_Data}, request))
