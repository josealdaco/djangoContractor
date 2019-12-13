from .models import wikiPagesModel
from .config import SECRET_KEY_DiffBot, SECRET_KEY_NEWS   #  Keeping my API Key a SECRET_KEY :)
import requests


def updateApp():
    context = {}
    data_dict = {}
    title_list = ['Oceans', 'Trees', 'Hunger', 'Globalwarming']
    for item in title_list:
        params = {
                'q': item,
                'from': '2019-12-12',
                'sortBy': 'popularity',
                'apiKey': SECRET_KEY_NEWS
        }
        response2 = requests.get('https://newsapi.org/v2/everything?', params)
        data = response2.json()['articles'][0]['url']  #  Get list of pages
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
                      'fundOneTitle': title_list[0],
                      'fundTwoURL': context.get(title_list[1]),
                      'fundTwoTitle': title_list[1],
                      'fundThreeURL': context.get(title_list[2]),
                      'fundThreeTitle': title_list[2],
                      'fundFourTitle': title_list[3],
                      'fundFourURL': context.get(title_list[3])})
    m = wikiPagesModel(**data_dict)
    m.save()
    for objects in wikiPagesModel.objects.all():
        if objects.id != 1:
            wikiPagesModel.objects.get(id=objects.id).delete()
    return
