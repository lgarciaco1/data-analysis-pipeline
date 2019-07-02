import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p
import matplotlib.dates as mdates

def media_movil(df_final):
    df_final['Date'] = pd.to_datetime(df_final['Date'])
    comp=input("\nIntroduce the name of the company you would like to plot: ")
    comp=comp.lower()
    df_subset=df_final[df_final["company"]==comp]
    lst2=[]
    for i in range(2):
        window=int(input("\nIntroduce window number {0}: ".format(i+1)))
        lst2.append(window)

    print("\nrange: {0}  -  {1}".format(df_subset["Date"].values[0],df_subset["Date"].values[-1]))
    start_date = input("\nIntroduce start date: ")
    end_date=input("\nIntroduce end date: ")
    df_subset1 = df_subset[(df_subset['Date'] > start_date) & (df_subset['Date'] <= end_date)]

    rolling_mean = df_subset1["Close"].rolling(window=lst2[0]).mean()
    rolling_mean2 = df_subset1["Close"].rolling(window=lst2[1]).mean()

    plt.plot(df_subset1["Date"], df_subset1["Close"], label='AMD')
    plt.plot(df_subset1["Date"], rolling_mean, label='AMD 20 Day SMA', color='orange')
    plt.plot(df_subset1["Date"], rolling_mean2, label='AMD 50 Day SMA', color='magenta')
    plt.title("Media Móvil")
    plt.legend(loc='upper left')
    plt.savefig('cotizacion.png')
    plt.show()
    return