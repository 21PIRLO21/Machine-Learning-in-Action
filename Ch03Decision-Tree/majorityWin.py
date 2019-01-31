'''
The minority is subordinate to the majority 
'''
import operator
def majorityWin(classlst):
	classCount = {}
	for vote in classlst:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), \
	key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]