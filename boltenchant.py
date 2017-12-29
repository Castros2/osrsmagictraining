import requests
import json

# Gets price of item from GE using the item id
def getPrice(id):
	# Get json returned from following url with item id concatenated into the url
	response = requests.get("http://services.runescape.com/m=itemdb_oldschool/api/graph/" + str(id) + ".json");
	# Use json library to load json into a json object (which happens to be a dict)
	# Content needs to be decoded because json returned from url is in byte format
	jsondict = json.loads(response.content.decode('UTF-8'))
	array = []

	# The dict contains 2 keys, daily and average. We want the numbers form daily.
	# Daily contains another dict with all the raw data
	# The data is simply in the form of 'time' : price
	# We want the price from the latest time so we add all the times to an array in order to get the latest time later.
	for key, value in jsondict.items():
		for key2, value2 in value.items():
			array.append(key2)

	# Sort times then get the price from the latest time which is the last (-1th) item in array
	array.sort()
	return jsondict['daily'][str(array[-1])]

print(getPrice(561))