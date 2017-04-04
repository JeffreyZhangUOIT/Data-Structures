'''import csv

with open('exercise-1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x = []
    y = []
    for row in readCSV:
        sepal_width = row[0]
        petal_width = row[1]

        x.append(sepal_width)
        y.append(petal_width)
    print(x)
    print(y)
#----------------------------------------------
import csv

with open('exercise-1.csv', 'rb') as csvfile:
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)  # rewind
    incsv = csv.reader(csvfile)
    if has_header:
        next(incsv)  # skip header row
    column = 1
    datatype = float
    data = (datatype(row[column]) for row in incsv)
    least_value = min(data)

print least_value

#---------------------------------------------------
import csv

with open('exercise-1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x = []
    y = []
    for row in readCSV:
        sepal_width = row[0]
        petal_width = row[1]

        x.append(sepal_width)
        y.append(petal_width)
    pairs = []
    # Iterate through rows starting at the 3rd row)
for i in range(1, 0):
    # Iterate through columns starting at the 3rd column
    pairs.append([sepal_width(i, j).value for j in range(1, 1)])
    print pairs
    #------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(x,y,c= cluster,s=50)
for i,j in centers:
    ax.scatter(i,j,s=50,c='red',marker='+')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.colorbar(scatter)

fig.show()


import pandas as pd
from StringIO import StringIO
Data = pd.read_csv("exercise-1.csv")
print(Data)
pd.read_csv(StringIO(Data), skiprows=[2], header=None)
print(Data)
'''

#!/usr/bin/python

# This program attend to read data from a csv file,
# and apply kmean, then output the result.

from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten

import csv

if __name__ == "__main__":

    # clusters
    K = 3

    sepal_width = []
    petal_width = []

    with open('exercise-1.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            sepal_width.append(float(x)for x in row[1:])
            petal_width.append([row[0]])

    x = vstack(sepal_width)
    y = vstack(petal_width)

    # normalization
    x = whiten(x)

    # computing K-Means with K (clusters)
    centroids, distortion = kmeans(x,3)
    print "distortion = " + str(distortion)

    # assign each sample to a cluster
    idx,_ = vq(x,centroids)

    # some plotting using numpy's logical indexing
    plot(x[idx==0,0], x[idx==0,1],'ob',
         x[idx==1,0], x[idx==1,1],'or',
         x[idx==2,0], x[idx==2,1],'og')

    print y
    print x

    for i in range(K):
        result_names = y[idx==i, 0]
        print "================================="
        print "Cluster " + str(i+1)
        for name in result_names:
            print name

    plot(centroids[:,0],
         centroids[:,1],
         'sg',markersize=8)

    show()