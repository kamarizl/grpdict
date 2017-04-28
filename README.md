# grpdict
group by selected key from list of dictionary

````python
listOfDictionary = [
	{"num": 1, "section": "A", "risk": "high"},
	{"num": 2, "section": "A", "risk": "high"},
	{"num": 3, "section": "B", "risk": "medium"}
]

data = Grpdict(listOfDictionary)
groupData = data.groupby("section")
print groupData
````

**output**

````
{'A': [{'num': 1, 'risk': 'high'}, {'num': 2, 'risk': 'high'}], 'B': [{'num': 3, 'risk': 'medium'}]}
````
