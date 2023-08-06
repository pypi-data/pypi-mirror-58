# Created: 12/19/2019
# Author:  Emiliano Jordan,
# Project: sejings

import sys

def in_doctest():
    """
    Determined by observation

    Thanks! https://stackoverflow.com/questions/8116118/
    how-to-determine-whether-code-is-running-in-a-doctest
    """
    if '_pytest.doctest' in sys.modules:
        return True
    ##
    if hasattr(sys.modules['__main__'], '_SpoofOut'):
        return True
    ##
    if sys.modules['__main__'].__dict__.get('__file__', '').endswith('/pytest'):
        return True
    ##
    return False