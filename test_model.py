import pickle
import sklearn
import pandas as pd

loaded_model = pickle.load(open("rf_model.sav", 'rb'))

mtest = pd.read_csv('mtest.csv')

columns = mtest.columns
t = pd.DataFrame(columns=columns)
t.loc[len(t)] = [40 for i in range(520)]
print(t)
print(loaded_model.predict(t))