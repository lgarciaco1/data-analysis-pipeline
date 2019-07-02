import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def incremento(df_final):

    df_final['Date'] = pd.to_datetime(df_final['Date'])

    num=2
    lst1=[]
    for i in range(num):
        comp1=input("\nIntroduce the name of company {0}: ".format(i+1))
        comp1=comp1.lower()
        lst1.append(comp1)

    subsetDataFrame = df_final[df_final['company'].isin(lst1) ]

    lst2=[]
    for i in range(num):
        dfprueba=subsetDataFrame[subsetDataFrame["company"]==lst1[i]]
        lst2.append(dfprueba[["Date","Close","company"]])
    
    df_subset3 = pd.merge(*lst2, on="Date")
    
    print("\nrange: {0}  -  {1}".format(df_subset3["Date"].values[0],df_subset3["Date"].values[-1]))
    start_date = input("\nIntroduce start date: ")
    end_date=input("\nIntroduce end date: ")
    df_subset4 = df_subset3[(df_subset3['Date'] >= start_date) & (df_subset3['Date'] <= end_date)]


    df_subset4['Close_x'] = df_subset4['Close_x'].astype(float)
    y=df_subset4.Close_x.values[0]
    df_subset4["return_x"] = df_subset4["Close_x"].apply(lambda x: x/y)

    df_subset4['Close_y'] = df_subset4['Close_y'].astype(float)
    z=df_subset4.Close_y.values[0]
    df_subset4["return_y"] = df_subset4["Close_y"].apply(lambda x: x/z)


    plt.plot(df_subset4['Date'], df_subset4['return_x'])
    plt.plot(df_subset4["Date"],df_subset4['return_y'])
    plt.title("Incremento porcentual en base {0}".format(start_date))
    plt.xlabel('Date')  
    plt.ylabel('% Change')  

    
    plt.savefig('cotizacion.png')
    plt.show()
    return