from sklearn.svm import SVC
import pickle

from utils import prepare_data

authenticated_pair = ['S13', 'S21']

all_data = prepare_data('./data', authenticated_pair)

df = all_data.drop(['timestamp','transmitter', 'receiver','Authenticated'],axis = 1)
dfy = all_data[['Authenticated']]


X_train = df
y_train = dfy

svc = SVC() 
svc.fit(X_train, y_train) 

filename = 'rf_model_class.sav'
pickle.dump(svc, open(filename, 'wb'))