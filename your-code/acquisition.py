
import pandas as pd

import pandas as pd
def companies(companies):
    lista_dfs = []
    for company in companies:
        df_temp = pd.read_csv('../spanish-stocks-historical-data/{0}.csv'.format(company))
        df_temp['company'] = company
        lista_dfs.append(df_temp)
    
    df_total = pd.concat(lista_dfs)
    return df_total