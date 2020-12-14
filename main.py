import datetime
import time


while True:
    myfile = open('/home/niklas/abc/time.txt', 'w+')
    date_now = datetime.datetime.now()
    myfile.write(str(date_now))

    time.sleep(5)
