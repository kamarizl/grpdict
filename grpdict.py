#!/usr/bin/env python


class Grpdict(object):
  """group selected key from a list of dictionary """

	def __init__(self, listOfDictionary):
		self.listOfDictionary = listOfDictionary

	def groupby(self, groupByThisKey):
		allKey = [x[groupByThisKey] for x in self.listOfDictionary]

		data = {}

		for selectedKey in set(allKey):
			data[selectedKey] = []
			for eachDictionary in self.listOfDictionary:
				if eachDictionary[groupByThisKey] == selectedKey:
					_eachDictionary = eachDictionary.copy()
					_eachDictionary.pop(groupByThisKey, None)
					data[selectedKey].append(_eachDictionary)

		return data


if __name__ == '__main__':
	data = Grpdict(listOfDictionary)
	groupData = data.groupby("section")
	print groupData


