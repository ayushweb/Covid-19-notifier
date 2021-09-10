import time 
from plyer import notification as ns
import requests
from bs4 import BeautifulSoup


def notifyme(title,message):
    ns.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Ayush\\Downloads\\covid19.ico",
        timeout = 8
    )

def getdata(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    while True:
        myhtmldata=getdata("https://www.mohfw.gov.in/")
    
        soup = BeautifulSoup(myhtmldata,'html.parser')
        mydatastr=""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            mydatastr+= tr.get_text()
        mydatastr=mydatastr[1:]
        itemlist=mydatastr.split("\n\n")
        states=['Bihar','Kerala','Jharkhand']
        for item in itemlist[0:22]:
            datalist=item.split("\n")
            if datalist[1] in states:
                nTitle="cases of covid-19"
                ntext= f"State:{datalist[1]}\ntotal active cases:{datalist[2]}\ntotal deaths:{datalist[4]}"
                notifyme(nTitle,ntext)
                time.sleep(3)
        time.sleep(200)