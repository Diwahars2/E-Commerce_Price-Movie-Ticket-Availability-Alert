# E-Commerce_Price-Movie-Ticket-Availability-Alert
Python script to get SMS notification, if the price of the Amazon product drops to your expected price and to get ticket details from BookMyShow

How does this work?

1.  It uses Beautifulsoup, lxml to get the product's price.
2.  If the current price is lower that expected price, through Twilio, it sends out a text message.
3.  It can be scheduled to run as a Cron job, based your need.


Improvements:

Have to test with Amazon Product Advertising API to get the product's price
Have to modify flipkart code and upload

Dependencies:

Before you get started, make sure you have installed:

Beautifulsoup4 (pip install Beautifulsoup4)
lxml (pip install lxml)
Twilio (pip install twilio)
