'''
Creat new dateset
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
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

