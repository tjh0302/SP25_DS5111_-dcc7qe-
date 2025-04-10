'''
This module holds the factory class.
'''
import sys
sys.path.append('.')
from bin.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.yahoo import GainerDownloadYahoo, GainerProcessYahoo

# FACTORY
class GainerFactory:
    '''
    This is the factory class for the gainers.
    '''
    def __init__(self, choice):
        '''
        Init method for the factory class for the gainers.
        '''
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        '''
        Gets the downloader specific to the data source. Method for the factory class.
        '''
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            download_var = GainerDownloadYahoo()
        else:
            download_var = GainerDownloadWSJ()
        return download_var

    def get_processor(self):
        '''
        Gets the processor specific to the data source. Method for the factory class.
        '''
        if self.choice == 'yahoo':
            process_var = GainerProcessYahoo()
        else:
            process_var = GainerProcessWSJ()
        return process_var
