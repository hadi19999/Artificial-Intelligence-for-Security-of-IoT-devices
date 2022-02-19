import pickle
import numpy as np
import pandas as pd
import time
from twofish import Twofish

from sklearn.linear_model import LogisticRegression
import pickle

class Receiver():

    def __init__(self, secret, model_name = None):
        self.model_trained = False
        self.setup_data()
        if model_name:
            self.load_model(model_name)
        self.twofish = Twofish(secret)

    def setup_data(self):
        csi_columns = ['A'+ str(i) for i in range(1,31)]
        self.columns = ['RSS'] + csi_columns + ['Authenticated']
        self.data = pd.DataFrame([], columns=self.columns)

    def decrypt(self, cipher):
        message = self.twofish.decrypt(cipher).decode()
        return message

    def save_data(self, input_data, authenticated):
        input_data.append(authenticated)
        data = pd.DataFrame([input_data], columns=self.columns)
        self.data = pd.concat([self.data, data])

    def train_model(self):
        regressor = LogisticRegression() 
        X_train = self.data.drop(['Authenticated'], axis = 1)
        y_train = self.data[['Authenticated']]
        regressor.fit(X_train.values.tolist(), y_train.values.tolist())
        filename = 'lr_model_class.sav'
        pickle.dump(regressor, open(filename, 'wb'))
    
    def load_model(self, model_name):
        print('Loading model ...')
        start = time.time()
        # Open existing model:
        # self.model = pickle.load(open('../models/' + model_name + '.sav', 'rb'))
        self.model = pickle.load(open(model_name + '.sav', 'rb'))

        end = time.time()
        print(model_name, f"loaded in {end - start} s!")

    def authenticate(self, input):
        start = time.time()
        authenticated = self.model.predict(np.array(input).reshape(1, -1))
        end = time.time()
        print('Time took for authentication (in second):', end - start)
        return authenticated

