import unittest
import sys
import os
#Add project root to path
sys.path.append("../..")
from SpeckleClient import SpeckleApiClient

class TestSpeckleStream(unittest.TestCase):

    def setUp(self):

        self.s = SpeckleApiClient()
        self.user = {"email":"testuser@arup.com","password":"testpassword", "username":"testuser"}

        login = self.s.UserLoginAsync(self.user)
        assert login, "Test User Login was not successful"

        self.user["id"] = login["resource"]["_id"]

        self.project = "5c7eb946be9a132091729f9e"
        self.stream = "RKWgU-oWF"
        
    def none_msg(self, header):
        return header + " responded with None"

    def test_get_project(self):
        r = self.s.ProjectGetAsync(self.project)
        self.assertIsNotNone(r, self.none_msg("ProjectGetAsync"))

    def test_update_project(self):
        data = {"name": "Amsterdam Project", "description": "this is an Amsterdam project modified by the API", "private": False}
        r = self.s.ProjectUpdateAsync(self.project, data)
        self.assertIsNotNone(r, self.none_msg("ProjectUpdateAsync"))

    def test_add_stream_to_project(self):
        r = self.s.ProjectAddStreamAsync(self.project, self.stream)
        self.assertIsNotNone(r, self.none_msg("ProjectUpdateAsync"))

    def test_ProjectCreateAsync(self):        
        project = {
        "owner": self.user["username"],
        "private": False,
        "anonymousComments": True,
        "canRead": [],
        "canWrite": [],
        "comments": [],
        "deleted": False,
        "resource": {},
        "text": "string",
        "assignedTo": [],
        "closed": True,
        "labels": [],
        "view": {},
        "screenshot": "string"
        }
        r = self.s.ProjectCreateAsync(project)
        self.assertIsNotNone(r, self.none_msg("ProjectCreateAsync"))

    def test_ProjectGetAllAsync(self):
        r = self.s.ProjectGetAllAsync(self)
        self.assertIsNotNone(r, self.none_msg("ProjectGetAllAsync"))

    def test_StreamCreateInsert(self):
        stream = {
        "owner": self.user["username"],
        "private": False,
        "anonymousComments": True,
        "canRead": [],
        "canWrite": [],
        "comments": [],
        "deleted": False,
        "streamId": "tu-asdasdasd",
        "name": "This is a Test Stream",
        "description": "I want to insert this stream into an existing project",
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

        current_project = {  
            "permissions":{  
                "canRead":[],
                "canWrite":[]
                },
            "private":False,
            "canRead":[],
            "canWrite":[],
            "anonymousComments":True,
            "comments":[],
            "name":"a sammple project",
            "description": "this is great",
            "tags":[],
            "streams":[],
            "deleted":False,
            "_id":"5c7eb946be9a132091729f9e",
            "text":"string",
            "assignedTo":[],
            "closed":True,
            "labels":[],
            "screenshot":"string",
            "owner":"5c5b576ce8cbae66eced0eaa",
            "createdAt":"2019-03-14T12:14:52.151Z",
            "updatedAt":"2019-03-14T12:14:52.151Z",
            "__v":0     
            }
        r = self.s.StreamCreateInsert(stream, current_project)
        self.assertIsNotNone(r, self.none_msg("StreamCreateInsert"))

if __name__ == "__main__":
    unittest.main()

