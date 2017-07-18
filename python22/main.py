import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url,full_name)

download_image("http://picua.org/img/2017-07/11/nmnp6xnfndyektbet7mjc2mox.png")
