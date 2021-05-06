import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import threading
import subprocess
import sched, time
import webbrowser


class GPU:
  def __init__(self, id_gpu, name):
    self.id_gpu = id_gpu
    self.name = name
    self.isOpen = False

  def getScraperLink(self):
    return f'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID={self.id_gpu}&SiteID=defaults'

  def getAMDlink(self):
    return f'https://www.amd.com/de/direct-buy/{self.id_gpu}/de'

def checkURL(dom, pos):
    if dom.__contains__("CAT_000015"):
        print(pos + "not available")
    else:
        # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Windows
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        # Linux
        # chrome_path = '/usr/bin/google-chrome %s'

        if (rx6800xt.name == pos) and (not rx6800xt.isOpen):
          rx6800xt.isOpen = True
          webbrowser.get(chrome_path).open(rx6800xt.getAMDlink())
        elif (rx6800xtMB.name == pos) and (not rx6800xtMB.isOpen):
          rx6800xtMB.isOpen = True
          webbrowser.get(chrome_path).open(rx6800xtMB.getAMDlink())
        elif (rx6800.name == pos) and (not rx6800.isOpen):
          rx6800.isOpen = True
          webbrowser.get(chrome_path).open(rx6800.getAMDlink())
        elif (rx6700xt.name == pos) and (not rx6700xt.isOpen):
          rx6700xt.isOpen = True
          webbrowser.get(chrome_path).open(rx6700xt.getAMDlink())
        elif (rx6900xt.name == pos) and (not rx6900xt.isOpen):
          rx6900xt.isOpen = True
          webbrowser.get(chrome_path).open(rx6900xt.getAMDlink())

        print(pos + "available")

def startAll():
  checkURL(BeautifulSoup(requests.get(rx6800xt.getScraperLink()).text, "html.parser").text, rx6800xt.name)
  checkURL(BeautifulSoup(requests.get(rx6800xtMB.getScraperLink()).text, "html.parser").text, rx6800xtMB.name)
  checkURL(BeautifulSoup(requests.get(rx6800.getScraperLink()).text, "html.parser").text, rx6800.name)
  checkURL(BeautifulSoup(requests.get(rx6900xt.getScraperLink()).text, "html.parser").text, rx6900xt.name)
  checkURL(BeautifulSoup(requests.get(rx6700xt.getScraperLink()).text, "html.parser").text, rx6700xt.name)
  print("--------------")

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    startAll()
    s.enter(5, 1, do_something, (sc,))

rx6800xt = GPU('5458374100','RX_6800_XT ',)
rx6800xtMB = GPU('5496921500', 'RX_6000XT_mb ')
rx6700xt = GPU('5496921400', 'RX_6800 ')
rx6800 = GPU('5458374000', 'RX_6900_XT ')
rx6900xt = GPU('5458374200', 'RX_6700_XT ')

s.enter(5, 1, do_something, (s,))
s.run()