import requests
import threading

class LoadDown():
    def __init__(self, url_list): #, url_list
        self.url_list = url_list

    def __iter__(self):
        self.a = -1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return self.url_list[x]

    def urllist_generator(self):
        return iter(self)

    def download(self, url, filename):
        r = requests.get(url)

        if r.status_code == 404:
            raise URLfour("Giver 404")

        return r

def get_url(url, filename):#, filename
    r = requests.get(url)
    print(r.json())
     
    with open(filename, 'wb') as fd:
        fd.write(r.content)
    
    print("Jeg er færdig")
    print("\n")
    print("\n")
    print("\n")

def download_multiple(url_list):
    for url in url_list:
        (threading.Thread(target=get_url, args=(url, url[24:27]+".txt"))).start()

class URLfour(ValueError):
    def __init__(self, arg):
        ValueError.__init__(self, arg)