"""
================================================================
Classification on the MUTAG dataset using the WL-subtree kernel.
================================================================

An example plot of :class:`grakel.GraphKernel`, :class:`grakel.WeisfeilerLehman`, :class:`grakel.VertexHistogram`
"""
from __future__ import print_function
print(__doc__)

from time import time

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import svm

from grakel import datasets
from grakel import GraphKernel

from matplotlib import pylab as pl

# Loads the Mutag dataset from:
# https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets
# the biggest collection of benchmark datasets for graph_kernels.
mutag = datasets.fetch_dataset("MUTAG", verbose=False)
G, y = mutag.data, mutag.target

# Train-test split of graph data
G_train, G_test, y_train, y_test = train_test_split(G, y, test_size=0.1, random_state=42)

start = time()
# Initialise a weifeiler kernel, with a dirac base_kernel.
gk = GraphKernel(kernel=[{"name": "WL", "n_iter": 5}, "ST-WL"], normalize=True)

# Calculate the kernel matrix.
K_train = gk.fit_transform(G_train)
K_test = gk.transform(G_test)
end = time()

# Initialise an SVM and fit.
clf = svm.SVC(kernel='precomputed', C=1)
clf.fit(K_train, y_train)

# Predict and test.
y_pred = clf.predict(K_test)

# Calculate accuracy of classification.
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", str(round(acc*100, 2)), "% | Took:",
      str(round(end - start, 2)), "s")

fig = pl.figure()
pl.subplot(121)
pl.imshow(K_train)
pl.subplot(122)
pl.imshow(K_test)
pl.show()

