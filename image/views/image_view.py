from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import FormView
from image.forms import ImageUploadForm
from django.contrib import messages


class ImageListView(View):
    def get(self, request):
        return render(request, "image/index.html")


class ImageUploadView(FormView):
    form_class = ImageUploadForm
    template_name = "image/index.html"
    success_url = reverse_lazy("index")

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            pass
        else:
            return self.form_invalid(form)
        return render(request, "image/index.html")

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_valid(form)
