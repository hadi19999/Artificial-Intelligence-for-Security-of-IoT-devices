from receiver import Receiver
from transmitter import Transmitter
import time

receiver = Receiver(b'*secret*')
transmitter = Transmitter(b'*secret*')

for i in range(150):
    # time.sleep(0.2)
    cipher = transmitter.encrypt('MESSAGE RECIEVED')
    rss_csi, authenticated = transmitter.get_random_data()
    receiver.save_data(rss_csi, authenticated)
    if receiver.model_trained:
        prediction = receiver.authenticate(rss_csi[:-1])
        print(prediction == authenticated)
    else:
        cipher = receiver.decrypt(cipher)
        print('decrypiton succeeded!')

    if i == 100:
        receiver.model_trained = True
        receiver.train_model()
        receiver.load_model('lr_model_class')

