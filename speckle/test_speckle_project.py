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

        login = self.s.UserLoginAsync(self.user)
        assert login, 'Test User Login was not successful'

        self.user['id'] = login['resource']['_id']

        self.project = '5c7eb946be9a132091729f9e'
        self.stream = 'RKWgU-oWF'
    def none_msg(self, header):
        return header + ' responded with None'

    def test_get_project(self):

        r = self.s.ProjectGetAsync(self.project)
        self.assertIsNotNone(r, self.none_msg('ProjectGetAsync'))

    def test_update_project(self):
        data = {'name': "Amsterdam Project", 'description': "This is an Amsterdam project modified by the API", 'private': False}
        r = self.s.ProjectUpdateAsync(self.project, data)

        self.assertIsNotNone(r, self.none_msg('ProjectUpdateAsync'))


    def test_add_stream_to_project(self):
        r = self.s.ProjectAddStreamAsync(self.project, self.stream)

        self.assertIsNotNone(r, self.none_msg('ProjectUpdateAsync'))
