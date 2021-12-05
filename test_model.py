import pickle
import sklearn
import pandas as pd
import os
import time

loaded_model = pickle.load(open("rf_model.sav", 'rb'))

mtest = pd.read_csv('mtest.csv')

def get_rss():
    columns = ["WAP"+str(i) for i in range(1,521)]
    stream = os.popen('iwlist wlp4s0 scanning')
    output = stream.read()
    level = output.split("Signal level=")[1].split(' dBm')[0]
    t = pd.DataFrame(columns=columns)
    t.loc[len(t)] = [100 for i in range(520)]
    t["WAP15"] = level
    return t
# print(t)

# while True:
#     print(get_rss())
#     time.sleep(5)
#     print(loaded_model.predict(get_rss()))

# def get_rss(u,k):
#     columns = ["WAP"+str(i) for i in range(1,521)]
#     t = pd.DataFrame(columns=columns)
#     t.loc[len(t)] = [100 for i in range(520)]
#     t["WAP"+str(k)] = u
#     return t
# for k in range(14,521):
#     print(-72,k, loaded_model.predict(get_rss(-72,k))[0][0])

print(get_rss())
