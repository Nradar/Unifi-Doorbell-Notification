import os
from twilio.rest import Client
import requests
from requests_html import HTML
from datetime import datetime

account_sid = "REDACTED"    #TWILLIO SID
auth_token = "REDACTED"     #TWILLIO TOKEN

client = Client(account_sid, auth_token)

def url_to_txt(url, filename="doorbell.html", save=False):
    r = requests.get(url)
    if(r.status_code == 200):
        html_text = r.text
        if save:
            with open(filename, 'w') as f:
                f.write(html_text)
        return html_text
    return ""


url = 'https://store.ui.com/collections/unifi-protect-accessories/products/uvc-g4-doorbell'
r = requests.get(url)

html_text = url_to_txt(url)
r_html = HTML(html=html_text)

form_class = ".bundleApp"   #class start with .
#form_id = "#NavDrawer" #id start with #
r_form = r_html.find(form_class)
# print(r_form)

if len(r_form) == 1:
    # print(r_form[0].text)
    r_bundle = r_form[0].find(".one-whole")
    # print(r_bundle[0].text)
    r_stock = r_bundle[0].text.splitlines()[2]
    # print(r_stock)
    if(r_stock == "Sold Out"):
        call = client.calls.create(
            from_="+13433077250",
            to="REDACTED",
            twiml='<Response><Say voice="Polly.Zhiyu" language="zh-CN">你的ubiquiti门铃到货啦！</Say></Response>'
        )

        message = client.messages.create(
            from_='+13433077250',
            to='+19059226646',
            body='你的ubiquiti门铃到货啦！赶紧前往官网下单！https://store.ui.com/collections/unifi-protect-accessories/products/uvc-g4-doorbell'
        )
        #print("instock")
    
    #record stock history
     n = datetime.now()
     f = open("/unfiStockCheck.txt", "a")
     f.write(r_stock)
     f.write(" ")
     f.write(str(n))
     f.write("\n")
     f.close()
