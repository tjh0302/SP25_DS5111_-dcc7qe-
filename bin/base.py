''' 
This file holds the base classes for the downloader and processor.
'''
from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC):
    '''
    This is the base class for the downloader.
    '''
    def __init__(self, url = ''):
        '''
        This is the init method for the base class for the downloader.
        '''
        self.url = url

    def print_attributes(self):
        '''
        Outputs attributes.
        '''
        print(self.__dict__)

    @abstractmethod
    def download(self):
        '''
        This is the abstract download method for the base class for the downloader.
        '''

# PROCESSORS
class GainerProcess(ABC):
    '''
    This is the base class for the gainer.
    '''
    def __init__(self):
        '''
        This is the init method for the base class for the gainer.
        '''

    @abstractmethod
    def normalize(self):
        '''
        This is the abstract normalize method for the base class for the gainer.
        '''

    @abstractmethod
    def save_with_timestamp(self):
        '''
        This is the save with timestamp method for the base class for the gainer.
        '''
