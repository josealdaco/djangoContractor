from django.conf.urls import url
# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views

urlpatterns = [
    url('charities', views.Homepage.as_view(), name='home')

]
