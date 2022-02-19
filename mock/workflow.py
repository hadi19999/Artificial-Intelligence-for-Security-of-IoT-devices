from receiver import Receiver
from transmitter import Transmitter
import time

receiver = Receiver(b'*secret*','rf_model_class')
transmitter = Transmitter(b'*secret*')

while True:
    time.sleep(1)
    rss_csi, authenticated = transmitter.get_random_data()
    prediction = receiver.authenticate(rss_csi)
    print(prediction, authenticated)
