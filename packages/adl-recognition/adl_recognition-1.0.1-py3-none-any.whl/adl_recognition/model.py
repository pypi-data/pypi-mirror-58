from keras.models import model_from_json
import os
import pkgutil


def get_model(model_path):
    model_json = pkgutil.get_data("adl_recognition", model_path + '.json')

    model = model_from_json(model_json)

    pkg_path = os.path.dirname(os.path.abspath(__file__))
    # load weights into new model
    model.load_weights(pkg_path + "/" + model_path + '.h5')
    return model
