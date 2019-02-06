import unittest
import sys
#Add project root to path
sys.path.append('../..')

from speckle.SpeckleClient import SpeckleApiClient


class TestSpeckleUser(unittest.TestCase):

    s = SpeckleApiClient()

    def test_get_stream(self):
        
        self.s.UserLoginAsync()