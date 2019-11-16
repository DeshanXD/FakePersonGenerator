import faster_than_requests as req
from glom import glom
import json

returnData = req.get2json_pretty("https://randomuser.me/api/")
returnData = json.loads(returnData)

#   Making file Name
lastName = returnData['results'][0]['name']['last']
firstName = returnData['results'][0]['name']['first']
personName = firstName + " " + lastName

# file = open(personName, "w+")

print(glom(returnData, 'results.0.gender'))