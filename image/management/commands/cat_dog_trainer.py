from django.core.management.base import BaseCommand
from fastai.vision.all import (
    untar_data,
    URLs,
    ImageDataLoaders,
    get_image_files,
    Resize,
    vision_learner,
    resnet34,
    error_rate,
)
from fastai.vision.all import *
import os
from fastcore.foundation import L
from core.settings import BASE_DIR


class Command(BaseCommand):
    help = "Train the cat dog identifier and save to disk"

    def handle(self, *args, **options):

        self.__execute()

        self.stdout.write(self.style.SUCCESS(f"Model trained and saved"))

    def __execute(self):
        path = untar_data(URLs.PETS) / "images"

        def is_cat(x):
            return x[0].isupper()

        # file_names: L = get_image_files(path)
        dls = ImageDataLoaders.from_name_func(
            path=path,
            fnames=get_image_files(path),
            valid_pct=0.2,
            seed=42,
            label_func=is_cat,
            item_tfms=Resize(224),
        )

        learn = vision_learner(dls, resnet34, metrics=error_rate)
        learn.fine_tune(1)

        """Colab Users
            * Uncomment the lines below if you wish to export to your google drive
        """
        # from google.colab import drive
        # drive.mount('/content/drive')
        # model_path = '/content/model.pkl'

        # comment this model_path if exporting to local drive.
        model_path = os.path.join(BASE_DIR, "image", "mldmodels", "cat_dog_model.pkl")
        learn.export(model_path)

        # Uncomment the lines below if exported to your drive and wish to download it

        # from google.colab import files
        # files.download("/content/model.pkl")
