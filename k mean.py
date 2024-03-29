import numpy as np
import random
# This script reads the points in CSV format
import csv

# Set up input and output variables for the script
with open('exercise-2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # Set up CSV reader and process the header
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)  # rewind
    incsv = csv.reader(csvfile)
    if has_header:
        next(incsv)  # skip header row
    column = 1
    datatype = float
    data = (datatype(row[column]) for row in incsv)

    # Make empty lists
    z = []
    y = []
    pair = []

    # Loop through the lines in the file and get each coordinate
    for row in readCSV:
        z = float(row[0])
        y = float(row[1])
        pair.append((z, y))


        # Print the coordinate list
print (pair)  # Ex.: pair[0][0] for the x  data in the 0 index
print(len(pair))

def cluster_points(X, mu):
    clusters = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x - mu[i[0]])) \
                         for i in enumerate(mu)], key=lambda t: t[1])[0]
        # print [(i[0], np.linalg.norm(x-mu[i[0]])) for i in enumerate(mu)]
        # print bestmukey
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters


def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis=0))
    return newmu


def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))


def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return (mu, clusters)


def init_board(N):
    X = np.array([(pair[i][0], pair[i][1]) for i in range(N)])
    return X


X = init_board(len(pair))

mu, clusters = find_centers(X, 4)

print mu

import matplotlib.pyplot as plt

xValues = []
yValues = []

for x in clusters:
    nextX = []
    nextY = []
    for point in clusters[x]:
        nextX.append(point[0])
        nextY.append(point[1])
    xValues.append(nextX)
    yValues.append(nextY)

colour = ["green", "blue", "red", "black"]

for i in range(0,len(mu)):
    plt.scatter(xValues[i], yValues[i], s=75, c=colour[i]) #xValues and yValues must be the same length
    plt.scatter(mu[i][0], mu[i][1], s=150, c=colour[i])
plt.show()
