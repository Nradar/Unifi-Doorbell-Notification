# Unifi-Doorbell-Notification

# Problem State

As I am currently setting up the ubiquiti environment in my home and looking forward to switch cloud recording doorbell(nest) to local host doorbell(unifi g4), unfortunately the ubiquiti doorbell is always in low stock, and restock every two weeks normally. I have missed several times when the doorbel back in stock. So I try to write a automated program to scraping the website information and tracking for the difference changed, when it detected back in stock it will make a phone call through the twillio API.
 
# Description

The program is run to notify you when the unifi G4 doorbell back instock. When it detect back instock, the program will send a message and make a call to your phone number, so that you will not miss the item. The program is based on python scrapy and twilio service. You need to get the twilio account first in order to make the program working.

# Run
- pip install requests
- pip install twilio
- python3 unifiDoorbell.py

Use crontab to run the program every minute, Further details about crontab please forward to https://en.wikipedia.org/wiki/Cron

# Error
The unifi website sometimes changes to prevent scrapy, sometimes it may not work perfectly.

# Result
Successfully got the doorbell by the help of the program !!!
