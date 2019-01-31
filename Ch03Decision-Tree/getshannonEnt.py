'''
get ShannonEnt
'''
from math import log
def ShannonEnt(dataset):
	setlenth = len(dataset)
	labels = {}
	for lst in dataset:
		nowlbl = lst[-1]
		if nowlbl not in labels.keys():        #<=>if nowlbl not in labels:
			labels[nowlbl] = 0
		else:
			labels[nowlbl] += 1
	shannonEnt = 0.0
	for key in labels.values():
		prob = float(key)/setlenth
		shannonEnt -= prob * log(prob,2)
	return shannonEnt