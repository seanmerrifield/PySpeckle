import unittest
import sys
import os
#Add project root to path
sys.path.append('../..')

from SpeckleClient import SpeckleApiClient


class TestSpeckleUser(unittest.TestCase):

    def setUp(self):

        self.s = SpeckleApiClient()
        self.user = {'email':'testuser@arup.com','password':'testpassword', 'username':'testuser'}

        self.test_stream = 'tu-sdfklj'
        assert self.s.UserLoginAsync(self.user), 'Test User Login was not successful'

    def none_msg(self, header):
        return header + ' responded with None'
    
    
    def test_get_all_streams(self):
        r = self.s.StreamsGetAllAsync()
        self.assertIsNotNone(r, self.none_msg('StreamGetAll'))


    def test_get_stream(self):
        stream_id = 'r1-uojnjm'
        r = self.s.StreamGetAsync(stream_id)
        self.assertIsNotNone(r, self.none_msg('StreamGetAsync'))


    def test_delete_stream(self):
        stream_id = self.test_stream

        r = self.s.StreamGetAsync(stream_id)
        if r == None: return
        
        r = self.s.StreamDeleteAsync(stream_id)
        self.assertIsNoneNone(r, self.none_msg('StreamDeleteAsync'))


    def test_create_stream(self):
        stream = {
        "_id": "5bcf2b693ff66c15abac3i5f",
        "owner": self.user['username'],
        "private": False,
        "anonymousComments": True,
        "canRead": [],
        "canWrite": [],
        "comments": [],
        "deleted": False,
        "streamId": "tu-sdfklj",
        "name": "test_stream",
        "objects": [{'_id': '5bcf2c7e3ff66c15abac431d', 'type': "Placeholder"}],
        "layers": [],
        "baseProperties": {},
        "globalMeasures": {},
        "isComputedResult": False,
        "viewerLayers": [],
        "parent": "string",
        "children": [],
        "ancestors": []
        }

        r = self.s.StreamCreateAsync(stream)

        self.assertIsNotNone(r, self.none_msg('StreamCreateAsync'))


    def test_create_object(self):

        obj_id = '5bcf2c7e3ff66c15abac431d'
        obj = {

        }

if __name__ == "__main__":
    unittest.main()