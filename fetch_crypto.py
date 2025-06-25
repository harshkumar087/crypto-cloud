from sqlalchemy import create_engine
import pandas as pd
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

# DB credentials
db_url = os.getenv('SUPA_URL')
engine = create_engine(db_url)

def automation():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': '20', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return

    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df.to_sql('crypto_table', engine, if_exists='append', index=False)

automation()
