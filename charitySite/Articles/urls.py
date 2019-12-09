from django.conf.urls import url

# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views

urlpatterns = [
    url('', views.Homepage.as_view()),


]
