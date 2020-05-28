from string import ascii_lowercase
import bs4
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections

def get_prehistoric_creatures(url):
    html = requests.get(url)
    txt = html.text
    soup = bs4.BeautifulSoup(txt, 'html.parser')
    events = soup.select('a font i')
    
    for e in events:
        print(e.getText())
        #return e.getText()
        
def get_all_prehistoric_creatures(base_url):
    animals = []
    
    for c in ascii_lowercase:
        scrape_url = base_url.format(c)
        animals.append(get_prehistoric_creatures(scrape_url))
    
    return animals

def get_DBA_price(name):
    base_url = 'https://www.dba.dk/'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)

    page_source = browser.page_source
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('td', {'title': 'Pris'})

    entries_str = []
    for e in event_cells:
        newE = e.text.replace('\n', '').replace('    ', '').replace(' kr.', '')
        entries_str.append(float(newE))
    
    print('gennemsnitspris for produkter på første side på DBA når man søger på ', name, ": ",  sum(entries_str)/len(entries_str))
    
def get_DBA_extreme_price(name):
    base_url = 'https://www.dba.dk/'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)

    page_source = browser.page_source
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('td', {'title': 'Pris'})

    entries_str = []
    for e in event_cells:
        newE = e.text.replace('\n', '').replace('    ', '').replace(' kr.', '')
        entries_str.append(float(newE))
    
    print('Højeste pris for produkter på første side på DBA når man søger på ', name, ": ",  max(entries_str))
    print('Laveste pris for produkter på første side på DBA når man søger på ', name, ": ",  min(entries_str))

def get_DBA_dates(name):
    base_url = 'https://www.dba.dk/'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)

    page_source = browser.page_source
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('td', {'title' : 'Dato'})

    entries_str = []
    for e in event_cells:
        newE = e.text.replace('\n    ', '').replace('\n', '')
        entries_str.append(newE)
     
    ctr = collections.Counter(entries_str)
    print(ctr)
