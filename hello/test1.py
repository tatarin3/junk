import threading

class messenger(threading.Thread):
    def run(self):
        for a in range(100):
            print(threading.currentThread().getName(),a*a)

x = messenger(name="LOLOLOLOL")
y = messenger(name="idknow WHAT TO DO!?!?!?")

x.start()
y.start()
