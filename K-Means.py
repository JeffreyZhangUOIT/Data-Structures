import numpy as np
import random
# This script reads the points in CSV format and
import csv

# Set up input and output variables for the script
with open('exercise-1.csv') as csvfile:
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
    x = []
    y = []
    pair = []

    # Loop through the lines in the file and get each coordinate
    for row in readCSV:
        x = float(row[0])
        y = float(row[1])
        pair.append((x, y))

    # Print the coordinate list
    print pair  # Ex.: pair[0][0] for the x  data in the 0 index

def cluster_points(X, mu):
    clusters = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x - mu[i[0]])) \
                         for i in enumerate(mu)], key=lambda t: t[1])[0]
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
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def init_board_gauss(N, k):
    n = float(N)/k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05,0.5)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) < 1 and abs(b) < 1:
                x.append([a,b])
        X.extend(x)
    X = np.array(X)[:N]
    return X