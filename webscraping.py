
import bs4
import requests

def get_prehistoric_creatures(url):
    html = requests.get(url)
    txt = html.text
    soup = bs4.BeautifulSoup(txt, 'html.parser')
    events = soup.select('a font i')
    
    for e in events:
        print(e.getText())