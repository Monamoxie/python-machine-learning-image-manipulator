from fastai.vision.all import load_learner
import os
from core.settings import BASE_DIR

"""
'/app/image/mlmodels/model.pkl'
'/app/image/media/mona.txt'
"""


# Define the custom function used in the model
def is_cat(x):
    return x[0].isupper()


globals()["is_cat"] = is_cat


class CatDogIdentifierService:
    def __init__(self) -> None:
        model_path = os.path.join(BASE_DIR, "image/mlmodels", "model.pkl")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"ML Model file not found at {model_path}")

        self.learn = load_learner(model_path)

    def predict(self, image: str):
        pred, _, probability = self.learn.predict(image)

        return pred
