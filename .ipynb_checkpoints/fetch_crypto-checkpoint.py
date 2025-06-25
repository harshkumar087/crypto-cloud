from sqlalchemy import create_engine
import pandas as pd
import os
from time import time
from time import sleep

# DB credentials

db_url = os.getenv( 'SUPA_URL' )

# Create engine
engine = create_engine(db_url)

def automation():
    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'20',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.getenv( 'API_KEY' ),
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df.to_sql('crypto_table', engine, if_exists='append', index=False)


for i in range (300):
    automation()
    print('queue:',i)
    sleep(120)
exit()