import pickle
import numpy as np
import time
from twofish import Twofish

class Receiver():

    def __init__(self, secret, model_name):
        self.load_model(model_name)
        self.twofish = Twofish(secret)

    def decrypt(self, cipher):
        message = self.twofish.decrypt(cipher).decode()
        return message

    def train_model(self):
        raise NotImplementedError
    
    def load_model(self, model_name):
        print('Loading model ...')
        start = time.time()
        self.model = pickle.load(open('../models/' + model_name + '.sav', 'rb'))
        end = time.time()
        print(model_name, f"loaded in {end - start} s!")

    def authenticate(self, input):
        start = time.time()
        authenticated = self.model.predict(np.array(input).reshape(1, -1))
        end = time.time()
        print('Time took for authentication (in second):', end - start)
        return authenticated


# input = [41, 23.08679276123039, 26.68332812825267, 32.14031735997639, 38.07886552931954, 39.66106403010388, 36.05551275463989, 35.90264614203248, 34.66987164671943, 33.24154027718932, 34.48187929913333, 35.0, 38.47076812334269, 41.773197148410844, 46.52956049652737, 43.60045871318328, 43.01162633521314, 44.204072210600685, 41.10960958218893, 39.84971769034255, 34.0147027033899, 34.17601498127012, 33.83784863137726, 40.01249804748511, 47.634021455258214, 46.14108798023731, 49.8196748283246, 42.42640687119285, 35.84689665786984, 37.44329045369811, 34.88552708502482]
# receiver = Receiver(b"*secret*", 'rf_model_class')
# T = Twofish(b'*secret*')
# x = T.encrypt(b'YELLOWSUBMARINES')
# print(receiver.decrypt(x))
# print(receiver.authenticate(input))