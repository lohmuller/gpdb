import unittest2 as unittest

import tinctest

from tinctest import TINCTestCase

@unittest.skip('mock test case for discovery tests')
class TINCRegressTestCase1(TINCTestCase):
    """
    
    @maintainer balasr3
    """
    def test_folder1_sample(self):
        pass
