#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
from time import sleep


#url = "http://www.amazon.in/gp/offer-listing/B00VBH9G8S/ref=dp_olp_new?ie=UTF8&condition=new"
url = "http://www.amazon.in/gp/offer-listing/B00Y0R9D6G/ref=dp_olp_new_mbc?ie=UTF8&condition=new"
threshold_prize = 4000
account = "ACa9b3e81772d45e7ef13da76e0cd907f3"
token = "6c5cfe377eb5ff9b79ddf1a371320178"
client = TwilioRestClient(account, token)

print("Fetching rates..")
while True:
  try:
    r = requests.get(url)
    while r.status_code is not 200:
      sleep(2)
      r = requests.get(url)

    soup = BeautifulSoup(r.text)
    #print soup
    data = soup.find("span",{"style":"text-decoration: inherit; white-space: nowrap;"}).contents[2]
    #data = soup.find('span',{'class':'a-size-base a-color-secondary a-text-normal'}).contents[2]
    print data
    data_int = float(data.replace(',',''))
    print data_int

    if data_int <= threshold_prize:
    #	Notify.init("Scorer")
    	client.messages.create(to="+919901035150",from_="+1201-992-8417",body="Product from Amazon:"+ data)
#    	scorer.show()
    
    sleep(500)

  except KeyboardInterrupt:
      break;
