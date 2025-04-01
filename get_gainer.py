'''
This file contains main and the template class.
'''
import sys
sys.path.append('.')
from bin.factory import GainerFactory

# TEMPLATE
class ProcessGainer:
    '''
    This is the template class.
    '''
    def __init__(self, gainer_downloader, gainer_normalizer):
        '''
        Init method of the process gainer class.
        '''
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer
        self.raw_df = None
        self.clean_df = None

    def print_attributes(self):
        '''
        Outputs an object's attributes.
        '''
        print(self.__dict__)

    def _download(self):
        '''
        Download method for the process gainer class.
        '''
        self.raw_df = self.downloader.download()

    def _normalize(self):
        '''
        Normalize method of the process gainer class.
        '''
        if 'raw_df' not in self.__dict__:
            self.raw_df = None
        self.clean_df = self.normalizer.normalize(self.raw_df)

    def _save_to_file(self):
        '''
        Method used to output a normalized file for the process gainer class.
        '''
        self.normalizer.save_with_timestamp()

    def process(self):
        '''
        Calls the 3 other class methods for the process gainer class.
        '''
        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":

    ##### Make our selection, 'one' choice
    choice = sys.argv[1]

    ##### let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    ##### create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
