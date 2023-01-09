from django.urls import path
from .views import *

urlpatterns=[
# path('',home,name='home'),
# path('get/',get_names)
path('',post_searchs,name='searchs')

]
