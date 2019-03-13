from .SpeckleClient import SpeckleApiClient
s = SpeckleApiClient()

import clr


#Grab Project Name
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
path = doc.PathName

OUT = (path.split('/')[-1]).split('.')[0]

#Grab Username
username = "test@arup.com"

#Grab Revit analytical geometry and properties

#for every analytical element
for el in elements:

    #Fill in object properties from the element
    obj_props = {
        "owner": username
        'type': "Mesh", 
        "name": "RevitFamily", 
        'applicationId': "RevitID", 
        'vertices': [], 
        'faces' = [], 
        'properties': {} , 
        
        }

    obj = {
            "private": False,
            "anonymousComments": True,
            "canRead": [],
            "canWrite": [],
            "comments": [],
            "deleted": False,
            "hash": "hash",
            "geometryHash": "Type.hash",
            "parent": None,
            "children": [],
            "ancestors": [],
            "transform": []
        }

    obj.extend(obj_props)

    objects.append(obj)

#Send objects to Speckle API
r = s.ObjectCreateAsync(objects)
assert r is not None and r['success'] == True, "Could not create Speckle Objects"

#Grab object Ids from response
obj_ids = [resource['_id'] for resource in r['resources']]


stream = {
    "owner": username,
    "private": False,
    "anonymousComments": True,
    "canRead": [],
    "canWrite": [],
    "comments": [],
    "deleted": False,
    "name": "sofistik_run",
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

#Create stream
r = s.StreamCreateAsync(stream)
assert r is not None and r['success'] == True, "Could not create Speckle Stream"

stream_id = r['resource']['_id']

#Add objects to stream
r = s.StreamAddObjectsAsync(stream_id, obj_ids)