import sys

def test_python_version():
    version = sys.version_info
    assert version >= (3, 10), "Python version needs to be 3.10 or 3.11"
    assert version <= (3, 11), "Python version needs to be 3.10 or 3.11"
