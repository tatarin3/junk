import threading

class Worker(threading.Thread):
    def run(self):
        for _ in range(1000):
            print('hello from',threading.current_thread().name)

for _ in range(10):
    thread = Worker()
    thread.start()
