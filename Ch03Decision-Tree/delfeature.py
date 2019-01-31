'''
del feature
'''
def delfeature(dataset, onedel, aa):
	leavedata = []
	for feature in dataset:
		if feature[onedel] == aa:
			reducefeat = feature[:onedel]
			reducefeat.extend(feature[onedel+1:])
			leavedata.append(reducefeat)
	return leavedata