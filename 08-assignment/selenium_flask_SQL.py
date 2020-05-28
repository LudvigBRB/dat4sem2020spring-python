from flask import Flask, jsonify, abort, request
import datetime
import mysql.connector
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections
from time import sleep

app = Flask(__name__)

def make_list(list, *options):
    entries_str = []
    for e in list:
        if options[0] == 1:
            newE = e.text.replace('\n', '').replace('    ', '').replace(' kr.', '')
            
            if len(newE) < 8:
                entries_str.append(float(newE))
            
        if options[0] == 2:
            newE = e.text.replace('\n    ', '').replace('\n', '')
            entries_str.append(newE)
            
    return entries_str

def get_DBA_info(name):
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
    prices = soup.find_all('td', {'title': 'Pris'})
    dates = soup.find_all('td', {'title' : 'Dato'})

    price_list = make_list(prices, 1)
    date_list = make_list(dates, 2)
    
    return price_list, date_list

def get_DBA_average_price(name):
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
    prices = soup.find_all('td', {'title': 'Pris'})

    price_list = make_list(prices, 1)
    
    return sum(price_list)/len(price_list)

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
    
    return max(entries_str), min(entries_str)

def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                              host='127.0.0.1',
                              port='3307',
                              database=database, 
                              use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx



@app.route('/')
def index():
    return 'Sådan virker denne webserver: \n skriv sql/avg/<søgeterm> for at få gennemsnitsprisen på <søgeterm> og indsætte dette i databasen \n skriv sql/all/<søgeterm> for at få pris og data på alle instanser af <søgeterm> og indsætte dem i databasen'

@app.route('/sql/<string:search_term>') #insert date and price for all instances of search_term on the first page into the database 
def insert_into_sql(search_term):
    prices, dates = get_DBA_info(search_term)

    cursor, cnx = make_SQL_cursor('pythondemo')

    query = ("INSERT INTO dba VALUES (null, %s, %s)")

    for i in range(len(prices)):
        cursor.execute(query, (dates[i], prices[i]))
    
    cnx.commit()
    
    cursor.close()
    cnx.close()

    return 'færdig' 

@app.route('/sql/avg/<string:search_term>') #insert average price of search_term of all instances on the first page
def insert_sql_average(search_term):
    avg_price = get_DBA_average_price(search_term)

    cursor, cnx = make_SQL_cursor('pythondemo')

    query = ("INSERT INTO avg_dba VALUES (null, %s, %s)")

    cursor.execute(query, (avg_price, search_term))

    cnx.commit()
    
    cursor.close()
    cnx.close()

    return 'færdig' 

@app.route('/sql/extr/<string:search_term>') #insert max and min price for <search_term> into database
def insert_sql_extreme(search_term):
    maxi, mini = get_DBA_extreme_price(search_term)
           
    cursor, cnx = make_SQL_cursor('pythondemo')
     
    query = ("INSERT INTO extreme_dba VALUES (null, %s, %s, %s)")
     
    cursor.execute(query, ( search_term, maxi, mini))
           
    cnx.commit()
    
    cursor.close()
    cnx.close()

    return 'færdig' 
           


if __name__ == '__main__':
    app.run(debug=True)