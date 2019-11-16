import faster_than_requests as req
from glom import glom
import json

returnData = req.get2json_pretty("https://randomuser.me/api/")
returnData = json.loads(returnData)
print("Gathered Data From Server")

#   Making file Name
lastName = glom(returnData, 'results.0.name.first')
firstName = glom(returnData, 'results.0.name.last')
personName = firstName + " " + lastName

file = open(personName, "w+")

print(glom(returnData, 'results.0.gender'))


def writeDatatoFile(argument, value, file):
    value = glom(returnData, value)
    wstring = argument + " : " + value
    file.write(wstring)
