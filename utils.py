from scipy.io import loadmat
import pandas as pd
import numpy as np
import os
from pathlib import Path

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

def prepare_data(directory, authenticated_pair):
    print('Preparing data ...')
    csi_columns = ['A'+ str(i) for i in range(1,31)]
    columns = ['timestamp', 'transmitter', 'receiver', 'RSS'] + csi_columns
    all_data = pd.DataFrame([], columns=columns)
    for p in getListOfFiles(Path(directory)):
        pair = p.split('/')[1]
        print(p, pair.split('_')[0], pair.split('_')[1])
        data = get_data(p, pair.split('_')[0], pair.split('_')[1], authenticated_pair = authenticated_pair)
        all_data = pd.concat([all_data, data])
    return all_data
