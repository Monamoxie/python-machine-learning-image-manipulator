import os
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import FormView
from core.services.cat_dog_identifier_service import CatDogIdentifierService
from image.forms import ImageUploadForm
from django.contrib import messages
from core.settings import BASE_DIR


class ImageListView(View):
    def get(self, request):
        return render(request, "image/index.html")


class ImageUploadView(FormView):
    form_class = ImageUploadForm
    template_name = "image/index.html"
    success_url = reverse_lazy("index")

    def post(self, request):

        form = ImageUploadForm(request.POST, request.FILES)
        service = CatDogIdentifierService()

        if form.is_valid():
            upload_dir = os.path.join(BASE_DIR, "image/media/uploads/")
            if not os.path.exists(upload_dir):
                os.mkdir(upload_dir)

            file = request.FILES["file"]

            with open(upload_dir + file.name, "wb+") as dest:
                for chunk in file.chunks():
                    dest.write(chunk)

            if os.path.exists(file_path := upload_dir + file.name):
                prediction = service.predict(file_path)

        else:
            return self.form_invalid(form)
        return render(request, "image/index.html")

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_valid(form)
