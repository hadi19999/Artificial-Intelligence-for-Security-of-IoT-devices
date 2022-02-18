from scipy.io import loadmat
import pandas as pd


annots = loadmat('data.mat')
# print(type(annots['Raw_Cell_Matrix']),annots['Raw_Cell_Matrix'].shape)
# print(annots['Raw_Cell_Matrix'][0][0]['RSSI_b'][0], annots['Raw_Cell_Matrix'][0][0]['RSSI_b'][0])
for item in annots['Raw_Cell_Matrix'][0][0]:
    print(item[0][0][0][0])
# print(annots['Raw_Cell_Matrix'][0][0]['CSI'][0][0][0][0])

data = []
for i in range(1778):
    # print(
    #     'S13', # transmitter
    #     'S21', # receiver
    #     # annots['Raw_Cell_Matrix'][i][0]['Nrx'][0][0][0][0], # Antennas  receiver side
    #     # annots['Raw_Cell_Matrix'][i][0]['Ntx'][0][0][0][0], # Antennas transmitter side
    #     annots['Raw_Cell_Matrix'][i][0]['agc'][0][0][0][0], # automatic gain control parameter of the NIC measured in dB
    #     # annots['Raw_Cell_Matrix'][i][0]['RSSI_a'][0][0][0][0], # RSS_a
    #     int(annots['Raw_Cell_Matrix'][i][0]['timestamp_low'][0][0][0][0]), # timestamp
    #     # annots['Raw_Cell_Matrix'][i][0]['label'][0][0][0][0], # label (can be ignored)
    #     annots['Raw_Cell_Matrix'][i][0]['CSI'][0][0][0][0] # CSI
    #     )

    data.append([
        int(annots['Raw_Cell_Matrix'][i][0]['timestamp_low'][0][0][0][0]),
        'S13',
        'S21',
        annots['Raw_Cell_Matrix'][i][0]['agc'][0][0][0][0],
        annots['Raw_Cell_Matrix'][i][0]['CSI'][0][0][0][0]]
        )

columns = ['timestamp', 'transmitter', 'receiver', 'agc', 'CSI']
df_train = pd.DataFrame(data, columns=columns)
print(df_train.head())
df_train.to_csv('data.csv')
# df_train.to_json('data.json')
