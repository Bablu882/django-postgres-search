from django.shortcuts import render
from django.http import JsonResponse
from .models import Searchname
from book.models import Book
from book.forms import PostSearchForm
from django.db.models import Q
import re
from metaphone import doublemetaphone


# def home(request):
#     form=PostSearchForm()
#     results=[]
#     if request.method=='GET':
#         form=PostSearchForm(request.GET)
#         if form.is_valid():
#             data=form.cleaned_data['q']
#             print(data)
#             # q_sum = Q()
#             # search_list =form.cleaned_data['q'].split(' ');
#             # print(search_list)
#             # for search_item in search_list:
#             #  search_regex = r"[[:space:]]%s[[:space:]]" % search_item
#             #  q_sum |= Q(title__iregex=search_regex)
#             #  results = Book.objects.filter(q_sum).distinct()
#             #  print(results)
            

#     return render(request,'engine/home.html',{'form':form,'results':results})


# def get_names(request):
#     search=request.GET.get('search')
#     print(search)
#     payload=[]
#     print(payload)
#     if search:
#         objs=Searchname.objects.filter(name__istartswith = search)

#         for obj in objs:
#             print(obj.name)
#             payload.append({'name':obj.name})
#     return JsonResponse({
#         'status':True,
#         'payload':payload
#     })

from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
import fuzzy
import re
from .documents import BookDocument
from elasticsearch_dsl import Q
def post_searchs(request):

    form = PostSearchForm()


    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():

            q = form.cleaned_data['q']
            query=q
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'title',
                    'authors'
                ],
                fuzziness='auto')
            results=BookDocument().search().query(q)
            # results=BookDocument.search().filter(Q('term',title=q)|Q('term',authors=q))
            # results = Book.objects.filter(title__sounds_like=q)
    return render(request,'engine/home.html',{'form':form,'results':results})



# from django_elasticsearch_dsl_drf.filter_backends import (
#     DefaultOrderingFilterBackend,
#     CompoundSearchFilterBackend,
#     OrderingFilterBackend,
# )
# from django_elasticsearch_dsl_drf.views import DocumentViewSet

# class BookCompoundFuzzySearchBackendDocumentViewSet(DocumentViewSet):
#    # ...
#     filter_backends = [
#         # ...
#         CompoundSearchFilterBackend,
#         # ...
#     ]

#     search_fields = {
#         'title': {'fuzziness': 'AUTO'},
#         'description': None,
#         'summary': None,
#     }