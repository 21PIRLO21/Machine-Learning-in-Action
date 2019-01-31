'''
This is a classifier
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math import log
import operator

def creatdataset(filename):
	yesorno = {'largeDoses':'2', 'smallDoses':'1', 'didntLike':'0'}
	fr = open(filename)
	alldata = fr.readlines()
	usingdata = alldata[:100]
	maxones = {'fly':0, 'gametime':0, 'ice':0}
	lstdata = []
	labelyesorno = []
	for line in usingdata:
		line = line.strip()
		listfromline = line.split('\t')
		lstdata.append(map(float, listfromline[:3]))          #numpy is better
		if(listfromline[-1].isdigit()):
			labelyesorno.append(int(listfromline[-1]))
		else:
			labelyesorno.append(yesorno.get(listfromline[-1]))
	trlst = zip(*lstdata)                         #lstdata.zip() is wrong
	maxones['fly'] = max(trlst[0])/2
	maxones['gametime'] = max(trlst[1])/2
	maxones['ice'] = max(trlst[2])/2
	for j in lstdata:
		if j[0] <= maxones['fly']:
			j[0] = 0
		else:
			j[0] = 1
	for j in lstdata:
		if j[1] <= maxones['gametime']:
			j[1] = 0
		else:
			j[1] = 1
	for j in lstdata:
		if j[2] <= maxones['ice']:
			j[2] = 0
		else:
			j[2] = 1
	for i in range(100):
		lstdata[i] += labelyesorno[i]
	return lstdata

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

def delfeature(dataset, onedel, aa):
	leavedata = []
	for feature in dataset:
		if feature[onedel] == aa:
			reducefeat = feature[:onedel]
			reducefeat.extend(feature[onedel+1:])
			leavedata.append(reducefeat)
	return leavedata

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

def majorityWin(classlst):
	classCount = {}
	for vote in classlst:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), \
	key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
