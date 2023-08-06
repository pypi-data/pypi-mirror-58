"""
========================================================================================
Classifying handwritten digits using the neighborhood subgraph pairwise distance kernel.
========================================================================================
Script makes use of :class:`grakel.NeighborhoodSubgraphPairwiseDistance`
"""
from __future__ import print_function
print(__doc__)

import numpy as np
import time
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

from grakel.kernels import NeighborhoodSubgraphPairwiseDistance
from grakel import Graph

digits = load_digits()

images = digits.images
n_samples, height, width = images.shape
y = digits.target
for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.axis('off')
    plt.imshow(images[i], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % y[i])

print("Transforming images to graphs\n")
graphs = list()
edges = list()
edge_labels = dict()
for i in range(height):
    for j in range(width):
        if j < width-1:
            edges.append((i*height+j, i*height+j+1))
            edge_labels[(i*height+j, i*height+j+1)] = 1
        if i < height-1:
            edges.append((i*height+j, (i+1)*height+j))
            edge_labels[(i*height+j, (i+1)*height+j)] = 2

for i in range(n_samples):
    node_labels = dict()
    for j in range(height):
        for k in range(width):
            node_labels[j*height+k] = int(images[i,j,k]/4)
    
    graphs.append(Graph(edges, node_labels=node_labels, edge_labels=edge_labels))

print("Splitting dataset into train/test (1000/100 instances)\n")
graphs_train, graphs_test = graphs[:1000], graphs[1000:1100]
y_train, y_test = y[:1000], y[1000:1100]

# Initialize neighborhood subgraph pairwise distance kernel
gk = NeighborhoodSubgraphPairwiseDistance(r=3, d=2)

print("Computing kernel matrics\n")
t0 = time.time()
K_train = gk.fit_transform(graphs_train)
K_test = gk.transform(graphs_test)
print("done in %0.3fs\n" % (time.time() - t0))

print("Classifying digits\n")
# Initialize SVM
clf = SVC(kernel='precomputed')

# Fit on the train Kernel
clf.fit(K_train, y_train)

# Predict and test.
y_pred = clf.predict(K_test)

# Calculate accuracy of classification.
print("Classification accuracy: %0.2f" % accuracy_score(y_test, y_pred))