from sklearn.linear_model import LogisticRegression
import pickle
import time

from utils import prepare_data

authenticated_pair = ['S13', 'S21']

all_data = prepare_data('./data', authenticated_pair)

df = all_data.drop(['timestamp','transmitter', 'receiver','Authenticated'],axis = 1)
dfy = all_data[['Authenticated']]


X_train = df
y_train = dfy

regressor = LogisticRegression() 
start = time.time()
regressor.fit(X_train, y_train)
end = time.time()
print(f"Training Time: {end - start} s")

filename = 'optimized_lr_model_class.sav'
pickle.dump(regressor, open(filename, 'wb'))

authenticated_pair = ['S13', 'S21']
test_data = prepare_data('./test_data',authenticated_pair = authenticated_pair)
df_test = test_data.drop(['timestamp','transmitter', 'receiver','Authenticated'],axis = 1)
dfy_test = test_data[['Authenticated']]

X_test = df_test
Y_test = dfy_test

print('Accuracy:', regressor.score(X_test, Y_test))

from sklearn.metrics import confusion_matrix

start = time.time()
y_pred = regressor.predict(X_test)
end = time.time()
print(f"Prediction Time: {end - start} s")

print('Confusion Matrix: \n', confusion_matrix(Y_test, y_pred))

from sklearn.metrics import precision_score


print('Precision: ', precision_score(Y_test, y_pred, average='weighted'))

from sklearn.metrics import f1_score

print('F1 Score: ', f1_score(Y_test, y_pred, average='weighted'))