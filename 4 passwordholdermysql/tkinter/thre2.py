import threading


class exthread(threading.Thread):
    """docstring forexthread."""
    def run(self):
        for i in range(100):
            print(threading.currentThread().getName())
            print(i**i)


a = exthread(name="firstthread")
b = exthread(name="secondthread")

a.start()
b.start()
