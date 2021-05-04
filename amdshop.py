import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import threading
import subprocess

rx6800xt = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374100&SiteID=defaults'
rx6800xtMB = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5496921500&SiteID=defaults'
rx6700xt = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5496921400&SiteID=defaults'
rx6800 = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374000&SiteID=defaults'
rx6900xt = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374200&SiteID=defaults'
cpu = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5450881700&SiteID=defaults'



def checkURL(dom, pos):
    if dom.__contains__("CAT_000015"):
        print(pos + "not available")
    else:
        #os.system('afplay /System/Library/Sounds/Glass.aiff')
        #applescript = f'display dialog "{pos}available" with title "This is a pop-up window" '
        #applescript = applescript + 'with icon caution buttons {"OK"}'
        #subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        print(pos + "available")
        t.cancel()

def startAll():
  t.start()
  checkURL(BeautifulSoup(requests.get(rx6800xt).text, "html.parser").text, "RX_6800_XT ")
  checkURL(BeautifulSoup(requests.get(rx6800xtMB).text, "html.parser").text, "RX_6000XT_mb ")
  checkURL(BeautifulSoup(requests.get(rx6800).text, "html.parser").text, "RX_6800 ")
  checkURL(BeautifulSoup(requests.get(rx6900xt).text, "html.parser").text, "RX_6900_XT ")
  checkURL(BeautifulSoup(requests.get(rx6700xt).text, "html.parser").text, "RX_6700_XT ")
  checkURL(BeautifulSoup(requests.get(cpu).text, "html.parser").text, "Ryzen_5_5600x ")
  print("--------------")

t = threading.Timer(5.0, startAll)
startAll()


