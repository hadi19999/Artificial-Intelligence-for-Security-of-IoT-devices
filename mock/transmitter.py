from twofish import Twofish
from utils import prepare_data
from random import randint

class Transmitter():

    def __init__(self, secret):
        self.twofish = Twofish(secret)
        self.data = self.load_data()

    def load_data(self):
        authenticated_pair = ['S13', 'S21']
        all_data = prepare_data('./mock_data', authenticated_pair)
        all_data = all_data.drop(['timestamp','transmitter', 'receiver'], axis = 1)
        return all_data

    def encrypt(self, message):
        cipher = self.twofish.encrypt(message.encode())
        return cipher

    def get_random_data(self):
        random_number = randint(0,len(self.data.values.tolist()))
        data = self.data.values.tolist()[random_number]
        rss_csi = data[:-1]
        authenticated = data[-1]
        return rss_csi, authenticated


# transmitter = Transmitter(b'*secret*')
# rss_csi, authenticated = transmitter.get_random_data()
# print(rss_csi, authenticated)

# T = Twofish(b'*secret*')

# for i in range(10, 99):
#     messagee = 'MESSAGENUMBER ' + str(i)
#     # print('aa', messagee)
#     print(T.decrypt(transmitter.encrypt(messagee)).decode())

