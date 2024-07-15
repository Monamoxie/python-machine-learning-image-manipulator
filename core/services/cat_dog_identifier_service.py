from fastai.vision.all import load_learner
from fastai.vision.all import *
import os
from core.settings import BASE_DIR

"""
'/app/image/mlmodels/model.pkl'
'/app/image/media/mona.txt'
"""


class CatDogIdentifierService:
    def __init__(self) -> None:
        self.model_path = os.path.join(BASE_DIR, "image/mlmodels", "model.pkl")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"ML Model file not found at {self.model_path}")

    def predict(self, image: str):
        img = PILImage.create(image)
        self.learn = load_learner(self.model_path)

        pred, _, probability = self.learn.predict(img)

        return str(pred) == True
