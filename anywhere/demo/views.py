from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    template_name = 'demo/index.html'

    def get(self, request):
        return HttpResponse('This is a demo, that i have successfully deployed.')
