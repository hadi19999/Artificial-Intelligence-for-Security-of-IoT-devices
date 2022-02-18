import random
import time
import numpy as np
import pickle
from scipy.io import loadmat
import pandas as pd


filename = 'knn_model.sav'

model = pickle.load(open(filename, 'rb'))
# while True:
#     rss = [random.randint(40, 90)]
#     csi_amplitude = [random.randint(40, 90) for i in range(1,31)]
#     test = rss + csi_amplitude
#     time.sleep(1)
#     print(model.predict(np.array(test).reshape(1, -1)) > 0.5)

def get_csi_amplitudes(csi_value):
    csi_amplitudes = []
    for v in csi_value:
        amplitude = np.absolute(v)
        csi_amplitudes.append(amplitude)
    return csi_amplitudes

def get_data(mat_filename, transmitter, receiver, authenticated_pair = [' ',' ']):
    annots = loadmat(mat_filename)
    data = []
    for i in range(len(annots['Raw_Cell_Matrix'])):
        authenticated = False
        if transmitter == authenticated_pair[0] and receiver == authenticated_pair[1]:
            authenticated = True
        data.append([
            int(annots['Raw_Cell_Matrix'][i][0]['timestamp_low'][0][0][0][0]),
            transmitter,
            receiver,
            annots['Raw_Cell_Matrix'][i][0]['agc'][0][0][0][0]
            ] + get_csi_amplitudes(annots['Raw_Cell_Matrix'][i][0]['CSI'][0][0][0][0])
            + [authenticated]
            )

    csi_columns = ['A'+ str(i) for i in range(1,31)]
    columns = ['timestamp', 'transmitter', 'receiver', 'RSS'] + csi_columns + ['Authenticated']
    final_data = pd.DataFrame(data, columns=columns)
    return final_data

# data = get_data('s13_s21_test.mat', 'S13', 'S21', ['S13', 'S21'])
# for t in data.values.tolist():
#     t = t[3:34]
#     print(model.predict(np.array(t).reshape(1, -1)) > 0.5)