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

        self.test_stream = 'u_Gnn3_2d'
        r =  self.s.UserLoginAsync(self.user), 'Test User Login was not successful'
        assert r is not None and r[0]['success'], 'Could not log in user'
        r = r[0]
        self.token = r['resource']['apitoken']
        self.user_id = r['resource']['_id']

    def none_msg(self, header):
        return header + ' responded with None'
    
    
    def test_get_all_streams(self):
        r = self.s.StreamsGetAllAsync()
        self.assertIsNotNone(r, self.none_msg('StreamGetAll'))
        self.assertTrue(r['success'])
        self.assertTrue('resources' in r)

        resources = r['resources']
        self.assertTrue(len(resources) > 0)

    def test_get_stream(self):
        r = self.s.StreamGetAsync(self.test_stream)
        self.assertIsNotNone(r, self.none_msg('StreamGetAsync'))
        self.assertTrue(r['success'])
        self.assertTrue('resource' in r)

        resource = r['resource']


    def test_get_objects_stream(self):
        r = self.s.StreamGetObjectsAsync(self.test_stream)
        self.assertIsNotNone(r, self.none_msg('StreamGetObjectsAsync'))
        self.assertTrue(r['success'])
        self.assertTrue('resources' in r)

        resources = r['resources']

    # def test_delete_stream(self):
    #     stream_id = self.test_stream

    #     r = self.s.StreamGetAsync(stream_id)
    #     if r == None: return
        
    #     r = self.s.StreamDeleteAsync(stream_id)
    #     self.assertIsNoneNone(r, self.none_msg('StreamDeleteAsync'))


    def test_create_stream(self):
        stream = {
        "owner": self.user['username'],
        "private": False,
        "anonymousComments": True,
        "canRead": [],
        "canWrite": [],
        "comments": [],
        "deleted": False,
        "streamId": "tu-sdfklj",
        "name": "test_stream",
        "objects": [],
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
        self.assertTrue(r['success'])
        self.assertTrue(r['resource'])

        resource = r['resource']
        self.assertTrue(resource['_id'])
        self.assertTrue(resource['streamId'])

    def test_add_objects_to_stream(self):

        r = self.s.StreamGetAsync(self.test_stream)
        assert r is not None and r['success'] == True, 'Could not get stream'

        r = self.s.StreamCreate

if __name__ == "__main__":
    unittest.main()