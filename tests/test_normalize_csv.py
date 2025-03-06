'''
This module tests the other files in this repository.
# apply 6 month rule here.  If there were ten files and you opened one of the test files does the liner help?
# in this case something like `Test that we convert first pandas generated csv to known standard` would be better I think
'''
import sys
import pandas as pd
sys.path.append('.')
import bin.normalize_csv as normal

def test_normalize_yahoo():
    '''
    Tests whether the normalize_yahoo function returns the correct variable,
    and with the correct number of columns.
    '''
    assert isinstance(normal.yahoo_norm, pd.DataFrame), "Expected a pandas dataframe"
    assert len(normal.yahoo_norm.columns) == 4, "yahoo_norm has the incorrect number of columns."

def test_normalize_wsj():
    '''
    Tests whether the normalize_wsj function returns the correct variable,
    and with the correct number of columns.
    '''
    assert isinstance(normal.wsj_norm, pd.DataFrame), "Expected a pandas dataframe"
    assert len(normal.wsj_norm.columns) == 4, "wsj_norm has the incorrect number of columns."

# can't find the tests for OS and python version
