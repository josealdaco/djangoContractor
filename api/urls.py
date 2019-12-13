from django.urls import path

from api.views import WikiDetail

urlpatterns = [
    path('pages/', WikiDetail.as_view(), name='wikiDetail'),
]
