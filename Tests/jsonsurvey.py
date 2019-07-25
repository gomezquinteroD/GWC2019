#import the json library
import json

myDictionary = {"name" : "Dani", "age" : 20, "school" : "SCAD" }

jsonToPython = json.dumps(myDictionary)

print(jsonToPython)
