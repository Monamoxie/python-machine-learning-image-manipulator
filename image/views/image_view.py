from django.views import View
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import FormView
from image.forms import ImageUploadForm


class ImageListView(View):
    def get(self, request):
        return render(request, "image/index.html")


class ImageUploadView(FormView):
    form_class = ImageUploadForm
    template_name = "image/index.html"

    def post(self, request):
        # WIP
        return render(request, "image/index.html")
