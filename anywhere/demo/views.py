from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    template_name = 'demo/index.html'

    def get(self, request):
        text = """
            I hoped you can see the navbar above, that means bootstrap and django work well together.
            This is a way to see if bootrstrap css will work when deployed to python anwhere.
        """
        return render(request, self.template_name, {'text': text})