from bs4 import BeautifulSoup
import urllib2, cookielib
import re
#url = "https://in.bookmyshow.com/buytickets_v1/mothers-day-hyderabad/movie-hyd-ET00039836-MT/20160504"
url = "https://in.bookmyshow.com/buytickets/kabali-bengaluru/movie-bang-ET00039091-MT/20160722"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)

def getList():
    l = []
    s=[]
    webpage = urllib2.urlopen(req)

    soup = BeautifulSoup(webpage, 'html.parser')
    #result=re.findall('data-availability="A"',soup)
    line1=str(soup)
    # Shows = len(result)
    for anchor in soup.find_all('a', {"class" : "__venue-name"}):
        item = anchor.contents[1].contents[0]
        l.append(item)
        

    return l

if __name__ == "__main__":
    l = getList()
    for i in l:
        print i