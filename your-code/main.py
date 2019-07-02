import acquisition
import webscrapping
import incremento
import media_movil
import velas_japonesas
from select import *
import pdf


def createDf():
    companies=["abengoa","acciona","acerinox","acs","atresmedia","banco_sabadell","bankinter","bbva","bme","caixabank","colonial","enagas","fcc","ferrovial","grifols","iberdrola","inditex","indra","mapfre","mediaset","naturgy","red_electrica","repsol","sacyr","santander","siemens_gamesa","telefonica"]
    return acquisition.companies(companies)

def add(df_total):
    url="https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20180216"
    rows=webscrapping.getInfo(url)
    return webscrapping.cleanData(rows,df_total)

def main():
    df_total=createDf()

    df_final=add(df_total)
    

    #Lo he intentado de todas las maneras y no me deja crear una funcion que seleccione el gráfico que quiero visualizar.
    print("options:\n\t1) incremento\n\t2) media_movil\n\t3) velas_japonesas")
    select1=int(input("Select the graph you would like to plot: "))
    if select1==1:
        incremento.incremento(df_final)
        pdf.creoPDF()

    if select1==2:
        media_movil.media_movil(df_final)
        pdf.creoPDF()

    if select1==3:
        velas_japonesas.velas_japonesas(df_final)


if __name__=="__main__":
    main()