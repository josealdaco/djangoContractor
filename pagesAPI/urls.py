
from django.urls import path
# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views
urlpatterns = [
    path('', views.APIpage.as_view(), name='APIPageViewer'),
]
