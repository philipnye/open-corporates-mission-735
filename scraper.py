#!/usr/bin/env python

import scraperwiki

import json

from datetime import date
from bs4 import BeautifulSoup
import requests
#import turbotlib

source_url = "http://www.namfisa.com.na/insurers/"
sample_date = str(date.today())
#turbotlib.log("Starting scrape...") # optional debug logging
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html)
table = doc.find('table', id='box-table-a')

for tr in table.find('tbody').find_all('tr'):
    # Each tr element has two td elements.
    tds = tr.find_all('td')
    if not tds[0].text=="Name of insurer":
        record = {
            'name_of_insurer':tds[0].text,
            'principal_officer':tds[1].text,    
            'address':tds[2].text,
            'registration_number':tds[3].text,
            'phone_number':tds[4].text,
            'fax_number':tds[5].text,
            'email-address':tds[6].text,
            'sample_date': sample_date,   # mandatory field
            'source_url': source_url      # mandatory field
        }
        print json.dumps(record)
