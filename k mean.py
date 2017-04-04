#!/usr/bin/python
#
# K-means clustering using Lloyd's algorithm in pure Python.
# Written by Lars Buitinck. This code is in the public domain.
#
# The main program runs the clustering algorithm on a bunch of text documents
# specified as command-line arguments. These documents are first converted to
# sparse vectors, represented as lists of (index, value) pairs.

from collections import defaultdict
from math import sqrt
import random


def densify(x, n):
    """Convert a sparse vector to a dense one."""
    d = [0] * n
    for i, v in x:
        d[i] = v
    return d


def dist(x, c):
    """Euclidean distance between sample x and cluster center c.
    Inputs: x, a sparse vector
            c, a dense vector
    """
    sqdist = 0.
    for i, v in x:
        sqdist += (v - c[i]) ** 2
    return sqrt(sqdist)


def mean(xs, l):
    """Mean (as a dense vector) of a set of sparse vectors of length l."""
    c = [0.] * l
    n = 0
    for x in xs:
        for i, v in x:
            c[i] += v
        n += 1
    for i in xrange(l):
        c[i] /= n
    return c


def kmeans(k, xs, l, n_iter=10):
    # Initialize from random points.
    centers = [densify(xs[i], l) for i in random.sample(xrange(len(xs)), k)]
    cluster = [None] * len(xs)

    for _ in xrange(n_iter):
        for i, x in enumerate(xs):
            cluster[i] = min(xrange(k), key=lambda j: dist(xs[i], centers[j]))
        for j, c in enumerate(centers):
            members = (x for i, x in enumerate(xs) if cluster[i] == j)
            centers[j] = mean(members, l)

    return cluster

import pandas as pd

if __name__ == '__main__':
    file = 'exercise-1.csv'

    df = pd.read_csv(file, parse_dates=[0], header=None, names=['sepal_width', 'petal_width'])
