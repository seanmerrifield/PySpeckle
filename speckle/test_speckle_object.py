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

        self.test_stream = 'RKWgU-oWF'
        self.test_object = '5bcf2c7e3ff66c15abac431d'

        login = self.s.UserLoginAsync(self.user)
        assert login, 'Test User Login was not successful'

        self.user['id'] = login['resource']['_id']

        self.stream = self.s.StreamGetAsync(self.test_stream)
        obj = self.s.StreamGetObjectsAsync(self.test_stream)

        #for o in obj['resources']:
           # r = self.s.ObjectDeleteAsync(o['_id'])

        self.s.StreamUpdateAsync(self.test_stream, self.stream)

    def tearDown(self):
        self.s.StreamUpdateAsync(self.test_stream, self.stream)

    def none_msg(self, header):
        return header + ' responded with None'
    

    def test_get_object(self):
        r = self.s.ObjectGetAsync(self.test_object)

        self.assertIsNotNone(r, self.none_msg('ObjectGetAsync'))
        self.assertTrue(r['success'])
        
   
    def test_create_object(self):

        r = self.s.ObjectCreateAsync([{"owner": self.user['username']}])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        #Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

        print(resource['_id'])

        self.s.StreamAddObjectAsync(self.test_stream, resource['_id'])

    def test_create_point_object(self):
        obj  = {
            "owner": self.user['username'],
            "type": "Point",
            "hash": "hash",
            "value": [0,0,0]
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        #Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

        print(resource['_id'])

        self.s.StreamAddObjectAsync(self.test_stream, resource['_id'])

    def test_create_mesh_object(self):
        obj = {
            "owner": self.user['username'],
            "type": "Mesh",
            "geometryHash": "Mesh.66ec936fc8eb1844581db685e5672f79",
            "hash": "2e4d67853709316f17e3745cd700a9ed",
            "properties": {
                "center": {
                    "type": "Point",
                    "value": [
                        -2.326136578802356,
                        7.41377889150433,
                        0.01525474415516414
                    ],
                    "hash": "318e1a3b9bf16bf5711170b61b4cd144",
                    "geometryHash": "Point.8012f72d1fd49795101ab099b7dff3cb"
                },
                "area": 1.6718884716988291,
                "revitFamTYpe": "undefined"
            },
            "vertices": [
                -2.6709675788879395,
                7.420193672180176,
                0.007017634343355894,
                -2.6617817878723145,
                7.910780906677246,
                0.016628438606858253,
                -2.6525962352752686,
                8.401368141174316,
                0.026239242404699326,
                -2.6434104442596436,
                8.891955375671387,
                0.03585004433989525,
                -2.6342246532440186,
                9.382542610168457,
                0.04546085000038147,
                -2.507732629776001,
                6.9263834953308105,
                0.005644594319164753,
                -2.498547077178955,
                7.416970729827881,
                0.01319583784788847,
                -2.48936128616333,
                7.907557964324951,
                0.02074708230793476,
                -2.480175495147705,
                8.39814567565918,
                0.028298325836658478,
                -2.47098970413208,
                8.88873291015625,
                0.035849571228027344,
                -2.3444979190826416,
                6.432573318481445,
                0.004271554294973612,
                -2.3353121280670166,
                6.923160552978516,
                0.00976323802024126,
                -2.3261263370513916,
                7.413747787475586,
                0.015254922211170197,
                -2.3169405460357666,
                7.9043354988098145,
                0.020746605470776558,
                -2.3077549934387207,
                8.394922256469727,
                0.02623829059302807,
                -2.181262969970703,
                5.93876314163208,
                0.0028985145036131144,
                -2.172077178955078,
                6.42935037612915,
                0.006330638192594051,
                -2.162891387939453,
                6.919937610626221,
                0.009762762114405632,
                -2.1537058353424072,
                7.410524845123291,
                0.013194886036217213,
                -2.1445200443267822,
                7.9011125564575195,
                0.016627009958028793,
                -2.0180280208587646,
                5.444952964782715,
                0.0015254743630066514,
                -2.0088422298431396,
                5.935540199279785,
                0.002898038364946842,
                -1.9996565580368042,
                6.4261274337768555,
                0.0042706020176410675,
                -1.9904708862304688,
                6.916714668273926,
                0.00564316613599658,
                -1.9812850952148438,
                7.407302379608154,
                0.0070157297886908054
            ],
            "faces": [
                1,
                6,
                1,
                0,
                5,
                1,
                7,
                2,
                1,
                6,
                1,
                8,
                3,
                2,
                7,
                1,
                9,
                4,
                3,
                8,
                1,
                11,
                6,
                5,
                10,
                1,
                12,
                7,
                6,
                11,
                1,
                13,
                8,
                7,
                12,
                1,
                14,
                9,
                8,
                13,
                1,
                16,
                11,
                10,
                15,
                1,
                17,
                12,
                11,
                16,
                1,
                18,
                13,
                12,
                17,
                1,
                19,
                14,
                13,
                18,
                1,
                21,
                16,
                15,
                20,
                1,
                22,
                17,
                16,
                21,
                1,
                23,
                18,
                17,
                22,
                1,
                24,
                19,
                18,
                23
            ]
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        # Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

        print(resource['_id'])

        self.s.StreamAddObjectAsync(self.test_stream, resource['_id'])

    def test_line_object(self):
        obj = {
        "type": "Line",
        "value": [
            -5689.317811503128,
            -13716.87365524665,
            3448.9999880790538,
            -5688.317811503128,
            -13717.87365524665,
            3539.9999880790538
        ],
        }

        r = self.s.ObjectCreateAsync([obj])

        self.assertIsNotNone(r, self.none_msg('ObjectCreateAsync'))
        self.assertTrue(r['success'])
        self.assertTrue(r['resources'])

        # Check created object ID is in response
        resource = r['resources'][0]
        self.assertTrue(resource['_id'])

        print(resource['_id'])

        self.s.StreamAddObjectAsync(self.test_stream, resource['_id'])

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