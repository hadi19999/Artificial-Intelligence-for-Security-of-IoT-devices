from scipy.io import loadmat
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
import pickle


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

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
        authenticated = 0
        if transmitter == authenticated_pair[0] and receiver == authenticated_pair[1]:
            authenticated = 1
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

# print(prepare_data('data.mat','S13','S21'))

from pathlib import Path

def prepare_data(directory, authenticated_pair):
    csi_columns = ['A'+ str(i) for i in range(1,31)]
    columns = ['timestamp', 'transmitter', 'receiver', 'RSS'] + csi_columns
    all_data = pd.DataFrame([], columns=columns)
    for p in getListOfFiles(Path(directory)):
        pair = p.split('/')[1]
        print(p, pair.split('_')[0], pair.split('_')[1])
        data = get_data(p, pair.split('_')[0], pair.split('_')[1], authenticated_pair = authenticated_pair)
        all_data = pd.concat([all_data, data])
    return all_data

authenticated_pair = ['S13', 'S21']

all_data = prepare_data('./data', authenticated_pair)

df = all_data.drop(['timestamp','transmitter', 'receiver','Authenticated'],axis = 1)
dfy = all_data[['Authenticated']]


X_train = df
y_train = dfy

regressor = RandomForestClassifier() 
regressor.fit(X_train, y_train)

filename = 'rf_model_class.sav'
pickle.dump(regressor, open(filename, 'wb'))