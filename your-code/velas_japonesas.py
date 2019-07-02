import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import plotly 
import plotly.graph_objs as go
import matplotlib.pyplot as plt
plotly.tools.set_credentials_file(username='lgarciaco1', api_key='AcJ6Vmo1ko0vhudVWrfJ')


def velas_japonesas(df_final):
    companies=["acciona","acerinox","acs","atresmedia","banco_sabadell","bankinter","bbva","bme","caixabank","colonial","enagas","fcc","ferrovial","grifols","iberdrola","inditex","indra","mapfre","mediaset","naturgy","red_electrica","repsol","sacyr","santander","siemens_gamesa","telefonica","bitcoin"]
    comp=input("\nIntroduce the name of the company you would like to plot: ")
    comp=comp.lower()
    if comp in companies:
        df_subset=df_final[df_final["company"]==comp]
        print("\nrange: {0}  -  {1}".format(df_subset["Date"].values[0],df_subset["Date"].values[-1]))
        start_date = input("\nIntroduce start date: ")
        end_date=input("\nIntroduce end date: ")
        df_subset5 = df_subset[(df_subset['Date'] > start_date) & (df_subset['Date'] <= end_date)]

    else:
        print("Error, the selected company is not included.")
    
    
    trace = go.Candlestick(x=df_subset5['Date'],
                    open=df_subset5['Open'],
                    high=df_subset5['High'],
                    low=df_subset5['Low'],
                    close=df_subset5['Close'])
    data = [trace]
    py.iplot(data, filename='simple_candlestick')
    import webbrowser
    url="https://plot.ly/~lgarciaco1/0"
    webbrowser.open(url)
    
