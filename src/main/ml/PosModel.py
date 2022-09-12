from tensorflow.keras.models import Sequential
from tensorflow.keras import models

class PosModel:
    def __init__(self, model_location):
        # If the model does not exist, create an empty model
        if model_location is not None:
            try:
                self.model = models.load_model(model_location)
            except:
                print("Model at location [{0}] does not exist. Creating blank model".format(model_location))
                self.model = Sequential()
        else:
            self.model = Sequential()

    def get_model(self):
        return self.model

    def save_model(self, model_location):
        self.model.save(model_location)

    def add_layer(self, layer):
        self.model.add(layer)