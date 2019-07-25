import json

myDictionary = {"name" : "Alex", "age" : 23, "school" : "Rutgers" }

#open the json file, use 'w' for write mode
f = open("newj.json", "w")
#dump your list/dictionary into the file object
json.dump(myDictionary, f)
#close the file
f.close()
