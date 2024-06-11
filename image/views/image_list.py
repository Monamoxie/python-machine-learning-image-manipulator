from django.views import View
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render


class ImageListView(View):
    def get(self, request):
        return render(request, "image/index.html")
