#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
from time import sleep

#Poduct link to get the price
url = "http://www.amazon.in/gp/offer-listing/B00Y0R9D6G/ref=dp_olp_new_mbc?ie=UTF8&condition=new"
threshold_prize = 4000
account = ""
token = ""
client = TwilioRestClient(account, token)

print("Fetching rates..")
while True:
  try:
    r = requests.get(url)
    while r.status_code is not 200:
      sleep(2)
      r = requests.get(url)

    soup = BeautifulSoup(r.text)
    data = soup.find("span",{"style":"text-decoration: inherit; white-space: nowrap;"}).contents[2]
    print data
    data_int = float(data.replace(',',''))
    print data_int

    if data_int <= threshold_prize:
          client.messages.create(to="+919901035150",from_="+1201-992-8417",body="Product from Amazon:"+ data)
    sleep(500)

  except KeyboardInterrupt:
      break;
