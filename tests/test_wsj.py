import sys
import pandas as pd
sys.path.append('.')
from bin.factory import GainerFactory
from get_gainer import ProcessGainer

def test_normalize_wsj():
    '''
    Tests whether the normalize_wsj function returns the correct variable,
    and with the correct number of columns.
    '''
    factory = GainerFactory('wsj')
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner._normalize()

    assert isinstance(runner.clean_df, pd.DataFrame), "Expected a pandas dataframe"
    assert len(runner.clean_df.columns) == 4, "wsj_norm has the incorrect number of columns."
