from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Page


def index(request):

    context_dict = {}
    context_dict['pagelist'] = Page.objects.order_by('-date')

    return render(request, 'weather/index.html', context=context_dict)



