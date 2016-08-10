import getList
import subprocess
#from say import *
from twilio.rest import TwilioRestClient

#Enter your Twilio account SID and Auth Token
accountSid = "ACa9b3e81772d45e7ef13da76e0cd907f3"
authToken = "6c5cfe377eb5ff9b79ddf1a371320178"

myTwilioNumber = "+1201-992-8417"
destCellPhone = "+919901035150"

twilioClient = TwilioRestClient(accountSid, authToken)

def notify(l):
   # for i in range(100):
        print l
        message = "Tickets are up for sale in: "+l
        twilioClient.messages.create(to="+919901035150", from_="+12019928417",body= message)

l = getList.getList()
threaterList = ["Carnival Cinemas: Rockline Mall, Bangalore",
"Cinepolis: Bannerghatta Road",
"Cinepolis: ETA Mall, Magadi Road",
"Cauvery Theatre: Sankey Road",
"PVR: Soul Spirit Bellandur, Bengaluru",
"PVR: Arena Mahadevapura, Bengaluru",
"INOX: Forum Value Mall, Whitefield",
"INOX Lido: Off MG Road, Ulsoor",
"Cinepolis (Fun Cinemas): Cunningham Road",
"Gopalan Cinemas: Arch Mall, Mysore Road",
"Gopalan Cinemas: Bannerghatta Road",
"Gopalan Grand Mall: Old Madras Road",
"Gopalan Mall: Sirsi Circle",
"Gopalan Miniplex: Signature Mall, Old Madras Road",
"Innovative Multiplex: Marathahalli",
"INOX: Central, JP Nagar, Mantri Junction",
"INOX: Garuda Mall, Magrath Road",
"INOX: Garuda Swagath Mall, Jayanagar",
"INOX: Brookefield Mall",
"INOX: Mantri Square, Malleshwaram",
"Lakshmi Theatre: Tavarekere",
"Mukunda Dolby Atmos: M S Nagar",
"Manasa Digital 4K Cinema: Konanakunte",
"Maheshwari Digital 4K Cinema: Bannerghatta Road",
"PVR: Forum Gold, Bengaluru",
"PVR: Market City, Bengaluru",
"PVR: Forum, Bengaluru",
"PVR: Orion Gold, Bengaluru",
"PVR: Orion, Bengaluru",
"PVR: VR, Bengaluru",
"PVR: Regalia, Bengaluru",
"PVR: VR Gold, Bengaluru",
"PVR: Vaishnavi Sapphire Mall, Bengaluru",
"Q Cinemas: Whitefield, Bengaluru",
"Rex Theatre: Brigade Road",
"Sandhya Digital 4K Cinema: Madiwala"]

for i in threaterList:
    if i in l:
        notify(i)