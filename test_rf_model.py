
import random
import time
import numpy as np
import pickle

filename = 'rf_model_class.sav'

model = pickle.load(open(filename, 'rb'))
while True:
    rss = [random.randint(40, 90)]
    csi_amplitude = [random.randint(40, 90) for i in range(1,31)]
    test = rss + csi_amplitude
    time.sleep(3)
    print(model.predict(np.array(test).reshape(1, -1)))