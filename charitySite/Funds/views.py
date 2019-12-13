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
from .config import SECRET_KEY_DiffBot, SECRET_KEY_NEWS   #  Keeping my API Key a SECRET_KEY :)


class Homepage(View):
    """ Displays a scroll view with all the possible funds, request for an API before loading screen"""
    def get(self, request):
        """for item in title_list:
            params = {
                    'q': item,
                    'from': '2019-12-12',
                    'sortBy': 'popularity',
                    'apiKey': SECRET_KEY_NEWS
            }
            response2 = requests.get('https://newsapi.org/v2/everything?', params)
            data = response2.json()['articles'][0]['url']  #  Get list of pages
            Starting to call API
            diffbotparams = {'token': SECRET_KEY_DiffBot,
                             'url': data,
                             'paging': False,
                             'maxPages': 1,
                             'numPages': 1,
                             }
            response = requests.get('https://api.diffbot.com/v3/article?', diffbotparams)
            diffBot_Data = response.json()['objects'][0]['text']
            context.update({item: diffBot_Data})
        #  Brute force way to create model, will optimize later

        data_dict.update({'fundOneURL': context.get(title_list[0]),
                          'fundTwoURL': context.get(title_list[1]),
                          'fundThreeURL': context.get(title_list[2]),
                          'fundFourURL': context.get(title_list[3])})
        m = wikiPagesModel(**data_dict)
        m.save()
        for objects in wikiPagesModel.objects.all():
            if objects.id != 1:
                wikiPagesModel.objects.get(id=objects.id).delete()"""
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
