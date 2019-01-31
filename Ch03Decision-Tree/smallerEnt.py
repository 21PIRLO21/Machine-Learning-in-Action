'''
Make ShannonEnt smaller
'''
def smallerEnt(dataset):
	numfeatures = len(dataset[0]) - 1
	baseEnt = ShannonEnt(dataset)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numfeatures):
		featlst = [x[i] for x in dataset]
		uniqueVals = set(featlst)
		newEnt = 0.0
		for val in uniqueVals:
			subdataset = delfeature(dataset, i, val)
			prob = len(subdataset)/float(len(dataset))
			newEnt += prob * ShannonEnt(subdataset)
		infoGain = baseEnt - newEnt
		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
