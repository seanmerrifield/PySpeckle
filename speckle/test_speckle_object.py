import unittest
import sys
import os
#Add project root to path
sys.path.append('../..')

from SpeckleClient import SpeckleApiClient


class TestSpeckleStream(unittest.TestCase):

    def setUp(self):

        self.s = SpeckleApiClient()
        self.user = {'email':'testuser@arup.com','password':'testpassword', 'username':'testuser'}

        self.test_stream = 'tu-sdfklj'
        self.test_object = '5bcf2c7e3ff66c15abac431d'
        assert self.s.UserLoginAsync(self.user), 'Test User Login was not successful'

    def none_msg(self, header):
        return header + ' responded with None'
    

     def test_get_object(self):
        r = self.s.ObjectGetAsync(self.test_object)

        self.assertIsNotNone(r, self.none_msg('ObjectGetAsync'))
        self.assertTrue(r['success'])
        
   
    def test_create_object(self):

        obj = {
            "owner": self.user['username'],
            "private": False,
            "anonymousComments": True,
            "canRead": [],
            "canWrite": [],
            "comments": [],
            "deleted": False,
            "type": "Mesh",
            "hash": "hash",
            "geometryHash": "Type.hash",
            "applicationId": "GUID",
            "name": "Object Doe",
            "properties": {},
            "parent": None,
            "children": [],
            "ancestors": [],
            "transform": []
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        #Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])


if __name__ == "__main__":
    unittest.main()