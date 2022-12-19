from django.urls import path
from .views import *

urlpatterns=[
    path('search/',post_search, name='post_search'),

    
]

