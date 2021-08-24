import facebook
import requests
import pandas as pd 
import numpy as np
import plotly.express as px

# token temporario 

app_id = '828211274551338'
app_secret = '5d1f8782732476667c42d5e811c62a92'
user_short_token = 'EAALxQPbRkCoBADjrtpa7JrfaHPKza6H10n7cpJoZBguhTyZB5G73wJhByTy2v2kptOmW3c87TXxCZByZBdDZCSuD0WTmZB3IrRnO9UsLrdihcPPXZB8sYub0sgA64o2m2P7NEZAGJrvXySczoILk74ZAoFdc3EUFFrxo6mx3Va83caCbCOsw8J1tZAAJKYZAT4SiIcDFtNdZApFPG4MnDlQsoU4mhEcKHxo7dP6s72631h2vFwkcZA3Y52uEfWh7En0RPJH0ZD'

url  = 'http://graph.facebook.com/oauth/access_token'
parametros = {'grant_type': 'fb_exchange_token',
              'client_id': app_id,
              'client_secret': app_secret, 
              'fb_exchange_token': user_short_token}
resposta = requests.get(url, params=parametros)
print(resposta)



app_id ='Numero token app'
app_secret ='numero token api'
user_short_token ='senha'
url  = 'http://graph.facebook.com/oauth/access_token'
parametros = {'grant_type': 'fb_exchange_token',
              'client_id': app_id,
              'client_secret': app_secret, 
              'fb_exchange_token': user_short_token}
resposta = requests.get(url, params=parametros)
print(resposta)