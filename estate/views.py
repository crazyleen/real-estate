from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


MENU_LIST = [
    {"href" : "/estate/evaluate/", "name":"客户购房意愿评估"},
    {"href" : "/estate/desire/", "name":"客户购房意愿查询"},
    {"href" : "/estate/relation/", "name":"客户与中介关联性检测"},
    {"href" : "/estate/", "name":"标签系统查询"},
    {"href" : "/estate/", "name":"系统设置"},
    {"href" : "/estate/", "name":"帮助"},
    {"href" : "/estate/", "name":"关于"},
]

def index(request):
    context = {"menu_list" : MENU_LIST}
    return render(request, 'estate/index.html', context)

def evaluate(request):
    context = {"menu_list" : MENU_LIST}
    return render(request, 'estate/evaluate.html', context)

def desire(request):
    context = {"menu_list" : MENU_LIST}
    return render(request, 'estate/desire.html', context)

def relation(request):
    context = {"menu_list" : MENU_LIST}
    return render(request, 'estate/relation.html', context)
