import sys,os
from sklearn.metrics.pairwise import euclidean_distances

#distance between two points
def distance(point, centroid):
	return euclidean_distances(point, centroid)
datapoints =[]
centroids = []


f = open('data.hdfs','r')
for line in f:
	line = line.split('\t')
	datapoints.append((line[0],float(line[1].split(",")[0])))
	

for line in sys.stdin:
	i=0
	line = line.split('\t')
	centroids.insert(i,float(line[1].split(",")[0]))

for (recId, point ) in datapoints:
	if(euclidean_distances(point, centroids[0])>euclidean_distances(point, centroids[1])):
		label =0
	else:
		label = 1
	print('%s,%s' % (recId, label))	




