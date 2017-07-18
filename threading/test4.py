import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def good():
    with lock1:
        time.sleep(0.001)
        with lock2:
            print('good')

def bad():
    with lock1:
        with lock2:
            print('bad')


threading.Thread(target=good).start()
threading.Thread(target=bad).start()

