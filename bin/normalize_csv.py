'''
This module imports and normalizes data from two sources - yahoo and wsj,
then outputs a normalized csv file for both, separately.
'''

import re
import pandas as pd

# import the raw files
wsj = pd.read_csv('wjsgainers.csv')
yahoo = pd.read_csv('ygainers.csv')

# normalize the wsj data
def normalize_wsj(df):
    '''
    This function normalizes the wsj data.
    '''

    assert isinstance(df, pd.DataFrame), "Expected a dataframe"
    raw = df.copy()

    raw = raw[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
    raw.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    raw['symbol'] = raw['symbol'].apply(lambda x: x[x.find('('):])
    raw['symbol'] = raw['symbol'].apply(lambda x: re.sub('[( )]', '', x))

    assert len(raw.columns) == 4, "could not match up columns"
    return raw

wsj_norm = normalize_wsj(wsj)

# normalize the yahoo data
def normalize_yahoo(df):
    '''
    This function normalizes the yahoo data.
    '''
    assert isinstance(df, pd.DataFrame), "Expected a dataframe"
    raw = df.copy()

    raw = raw[['Symbol', 'Price', 'Change', 'Change %']]
    raw.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    raw['price'] = raw['price'].apply(lambda x: x[:x.find(' ')])
    raw['price'] = raw['price'].apply(lambda x: re.sub('[,]', '', x))
    raw['price_percent_change'] = raw['price_percent_change'].apply(lambda x: re.sub('[-+%]','',x))

    for col in ['price', 'price_change', 'price_percent_change']:
        raw[col] = raw[col].astype('float64')

    assert len(raw.columns) == 4, "could not match up columns"
    return raw

yahoo_norm = normalize_yahoo(yahoo)

# output the normalized files to csv
wsj_norm.to_csv('wsj_gainers_norm.csv')
yahoo_norm.to_csv('ygainers_norm.csv')
