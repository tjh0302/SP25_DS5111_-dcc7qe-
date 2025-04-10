'''
This file downloads and processes the yahoo data.
The yahoo classes inherit the base class.
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

# DOWNLOADER
class GainerDownloadYahoo(GainerDownload):
    '''
    This is the yahoo download class.
    '''
    def __init__(self):
        '''
        Init method for yahoo download class.
        '''
        self.url = 'yahoo'
        self.raw_df = None

    def print_attributes(self):
        '''
        Output the class attributes.
        '''
        print(self.__dict__)

    def download(self):
        '''
        Primary download method for yahoo download class.
        '''
        print("Downloading yahoo gainers")
        subprocess.run(['make', '-C', '.', 'ygainers.csv'],
capture_output=True, text=True, check=True, shell=False)
        tz = timezone('US/Eastern')
        now = datetime.now(tz)
        format_time = f'{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}'
        self.raw_df = pd.read_csv(f'ygainers_{format_time}.csv')
        return self.raw_df

# Processor
class GainerProcessYahoo(GainerProcess):
    '''
    This is the yahoo processor class.
    '''
    def __init__(self):
        '''
        Init method for yahoo processor class.
        '''
        self.raw_df = None
        self.clean_df = None

    def normalize(self, df_raw):
        '''
        This function tests normalizing the yahoo data.
        '''
        print("Normalizing yahoo gainers")

        if isinstance(df_raw, pd.DataFrame):
            self.raw_df = df_raw
        else:
            self.raw_df = pd.read_csv('ygainers.csv')

        self.clean_df = self.raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        self.clean_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        self.clean_df['price'] = self.clean_df['price'].apply(lambda x: x[:x.find(' ')])
        self.clean_df['price'] = self.clean_df['price'].apply(lambda x: re.sub('[,]', '', x))
        self.clean_df['price_percent_change'] = self.clean_df['price_percent_change'].apply(
lambda x: re.sub('[-+%]','',x))

        for col in ['price', 'price_change', 'price_percent_change']:
            self.clean_df[col] = self.clean_df[col].astype('float64')

        assert len(self.clean_df.columns) == 4, "could not match up columns"
        return self.clean_df

    def save_with_timestamp(self):
        '''
        This functions saves a normalized yahoo gainers file with timestamp.
        It will be saved in the root because I do not specify a folder.
        '''
        print("Saving Yahoo gainers")
        tz = timezone('US/Eastern')
        now = datetime.now(tz)
        format_date = f'{now.year}_{now.month}_{now.day}'
        format_time = f'{now.hour}_{now.minute}_{now.second}'

        self.clean_df.to_csv(f'yahoo_norm_{format_date}_{format_time}.csv')
