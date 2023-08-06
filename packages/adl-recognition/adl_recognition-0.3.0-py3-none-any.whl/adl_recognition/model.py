from keras.models import model_from_json
import os
import pkgutil


def getModel(modelPath):

    model_json = pkgutil.get_data("adl_recognition", modelPath + '.json')

    model = model_from_json(model_json)

    pkg_path = os.path.dirname(os.path.abspath(__file__))
    # load weights into new model
    model.load_weights(pkg_path + "/"+modelPath + '.h5')
    return model
