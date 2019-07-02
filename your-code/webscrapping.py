import requests
from bs4 import BeautifulSoup
import pandas as pd

def getInfo(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    rows = soup.find_all('tr', {'class': 'text-right'})
    return rows

def cleanData(rows,df_total):
    lst=[]
    for i in rows:
        lst.append(i.text.replace("\n"," ").split(" "))
    date=[]
    open1=[]
    high=[]
    low=[]
    close1=[]
    volume=[]
    market_cap=[]

    for i in lst:
        date.append(" ".join(i[1:4]))
        open1.append(i[4])
        high.append(i[5])
        low.append(i[6])
        close1.append(i[7])
        volume.append(i[8])
        market_cap.append(i[9])

    name=[]
    for i in range(len(lst)):
        name.append("bitcoin")



    bitcoin=pd.DataFrame(list(zip(date, close1, high, low, open1, volume, name)), 
                columns =['Date', 'Close','High','Low','Open','Volume', 'company']) 


    bitcoin["Date"]=bitcoin["Date"].apply(fun)
    

    df_final=pd.concat([df_total, bitcoin], ignore_index=True)
    return df_final

months={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
def fun(x):
    for e in months.items():
        if e[0] in str(x):
            fecha=str(x).replace(e[0],e[1]).replace(",","").replace(" ","-")
            return fecha[6:] + "-" + fecha[0:5]