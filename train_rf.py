from sklearn.ensemble import RandomForestClassifier
import pickle

from utils import prepare_data

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