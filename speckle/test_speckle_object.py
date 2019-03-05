import unittest
import sys
import os
#Add project root to path
sys.path.append('../..')

from speckle.SpeckleClient import SpeckleApiClient


class TestSpeckleStream(unittest.TestCase):

    def setUp(self):

        self.s = SpeckleApiClient()
        self.user = {'email':'testuser@arup.com','password':'testpassword', 'username':'testuser'}

        self.test_stream = 'tu-sdfklj'
        self.test_object = '5bcf2c7e3ff66c15abac431d'

        login = self.s.UserLoginAsync(self.user)
        assert login, 'Test User Login was not successful'

        self.user['id'] = login['resource']['_id']

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

    def test_create_point_object(self):
        obj  = {
            "owner": self.user['username'],
            "private": False,
            "anonymousComments": True,
            "canRead": [],
            "canWrite": [],
            "comments": [],
            "deleted": False,
            "type": "Point",
            "hash": "hash",
            "geometryHash": "Type.hash",
            "applicationId": "GUID",
            "name": "Object Doe",
            "properties": {},
            "parent": None,
            "children": [],
            "ancestors": [],
            "transform": [],
            "value": [0,0,0]
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        #Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

    def test_create_mesh_object(self):
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
            "transform": [],
            "vertices": [-2.6709675788879395,7.420193672180176,0.007017634343355894,-2.6617817878723145],
            "faces": [0,1,2,3]
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        #Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

    def test_update_object(self):
        
        geometry = {
            "vertices": [0.0, 1.0, 2.0, 3.0],
            "faces": [1,2,3]
        }

        props = {
            'type': 'RCSlab', 
            'material': 'Concrete'
        }
        data = {'properties': props}
        data.update(geometry)
        r = self.s.ObjectUpdateAsync(self.test_object, data)
        self.assertIsNotNone(r)

        #Todo: Look into why user is not authorized to update
        self.assertTrue(r['success'])

if __name__ == "__main__":
    unittest.main()