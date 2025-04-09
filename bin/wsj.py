'''
This file downloads and processes the wsj data.
The wsj classes inherit the base class.
'''
import warnings
import sys
import re
import subprocess
from datetime import datetime
from pytz import timezone
import pandas as pd
sys.path.append('.')
from bin.base import GainerDownload, GainerProcess
warnings.filterwarnings('ignore')

class GainerDownloadWSJ(GainerDownload):
    '''
    Download class for wsj.
    '''
    def __init__(self):
        '''
        WSJ download class init method.
        '''
        self.url = 'wsj'
        self.raw_df = None

    def print_attributes(self):
        '''
        prints attributes.
        '''
        print(self.__dict__)

    def download(self):
        '''
        WSJ download method for the download class.
        '''
        print("Downloading wsj gainers")
        subprocess.run(['make', '-C', '.', 'wsjgainers.csv'],
capture_output=True, text=True, check=True, shell=False)
        tz = timezone('US/Eastern')
        now = datetime.now(tz)
        self.raw_df = pd.read_csv(f'wsjgainers_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.csv')
        return self.raw_df

class GainerProcessWSJ(GainerProcess):
    '''
    Processor class for wsj.
    '''
    def __init__(self):
        '''
        Init method for the processor class.
        '''
        self.raw_df = None
        self.clean_df = None

    def normalize(self, df_raw):
        '''
        This function tests normalizing the wsj data.
        '''
        print("Normalizing WSJ gainers")

        if isinstance(df_raw, pd.DataFrame):
            self.raw_df = df_raw
        else:
            self.raw_df = pd.read_csv('wsjgainers.csv')

        self.clean_df = self.raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        self.clean_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        self.clean_df['symbol'] = self.clean_df['symbol'].apply(lambda x: x[x.find('('):])
        self.clean_df['symbol'] = self.clean_df['symbol'].apply(lambda x: re.sub('[( )]', '', x))

        assert len(self.clean_df.columns) == 4, "could not match up columns"
        return self.clean_df

    def save_with_timestamp(self):
        '''
        This functions saves a normalized wsj gainers file with timestamp.
        It will be saved in the root because I do not specify a folder.
        '''
        print("Saving WSJ gainers")
        tz = timezone('US/Eastern')
        now = datetime.now(tz)
        format_date = f'{now.year}_{now.month}_{now.day}'
        format_time = f'{now.hour}_{now.minute}_{now.second}'

        self.clean_df.to_csv(f'wsj_norm_{format_date}_{format_time}.csv')
