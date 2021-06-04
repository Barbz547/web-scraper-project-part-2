from flask import render_template, redirect, current_app as app, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from math import floor 
from bs4 import BeautifulSoup




@app.route('/', methods = ['GET'])
def scrape_stock_symbols(Letter):
    print('Beggining web scraping...')

    company_name = []
    company_ticker = []
    #Letter = Letter.upper()
    URL = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies=A'  # append letter for any ticker
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    odd_rows = soup.find_all('tr', attrs={'class': 'ts0'})
    even_rows = soup.find_all('tr', attrs={'class': 'ts1'})

    for i in odd_rows:
        row = i.find_all('td')
        company_name.append(row[0].text.strip())  # company name
        company_ticker.append(row[1].text.strip())  # company ticker

    for i in even_rows:
        row = i.find_all('td')
        company_name.append(row[0].text.strip())  # company name
        company_ticker.append(row[1].text.strip())  # company ticker

    return (company_name, company_ticker)

    (temp_name, temp_ticker) = scrape_stock_symbols('a')
    temp_name

    driver.close

    return jsonify({ 'message': 'it works'})
