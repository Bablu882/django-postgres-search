from django.shortcuts import render
from django.http import JsonResponse
from .models import Searchname
from book.models import Book
from book.forms import PostSearchForm
from django.db.models import Q
import re


def home(request):
    form=PostSearchForm()
    results=[]
    if request.method=='GET':
        form=PostSearchForm(request.GET)
        if form.is_valid():
            data=form.cleaned_data['q']
            print(data)
            # q_sum = Q()
            # search_list =form.cleaned_data['q'].split(' ');
            # print(search_list)
            # for search_item in search_list:
            #  search_regex = r"[[:space:]]%s[[:space:]]" % search_item
            #  q_sum |= Q(title__iregex=search_regex)
            #  results = Book.objects.filter(q_sum).distinct()
            #  print(results)
            

    return render(request,'engine/home.html',{'form':form,'results':results})


def get_names(request):
    search=request.GET.get('search')
    print(search)
    payload=[]
    print(payload)
    if search:
        objs=Searchname.objects.filter(name__istartswith = search)

        for obj in objs:
            print(obj.name)
            payload.append({'name':obj.name})
    return JsonResponse({
        'status':True,
        'payload':payload
    })