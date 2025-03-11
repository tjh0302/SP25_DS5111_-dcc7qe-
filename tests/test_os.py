'''
This module tests that the operating system is linux.
'''
from sys import platform

def test_os():
    '''
    Tests that the operating system is linux.
    '''
    os_result = platform
    assert os_result == 'linux', "The operating system is not linux"




