# GraKeL: A library for graph kernels

[![Pypi Versions](https://img.shields.io/pypi/pyversions/grakel-dev.svg)](https://pypi.org/pypi/grakel-dev/)
[![Coverage Status](https://codecov.io/gh/ysig/GraKeL/branch/develop/graph/badge.svg)](https://codecov.io/gh/ysig/GraKeL)
[![Travis Status](https://travis-ci.org/ysig/GraKeL.svg?branch=develop)](https://travis-ci.org/ysig/GraKeL)
[![Appveyor status](https://ci.appveyor.com/api/projects/status/sss4lpfxwgejn6de/branch/develop?svg=true)](https://ci.appveyor.com/project/ysig/grakel)
[![CircleCI Status](https://circleci.com/gh/ysig/GraKeL/tree/develop.svg?style=shield)](https://circleci.com/gh/ysig/GraKeL/tree/develop)

**GraKeL** is a library compatible with the project of [scikit-learn](http://scikit-learn.org/)

Installation
=================

The GraKeL library requires:

* Python (>=2.7, >=3.5)
* NumPy (>=1.8.2)
* SciPy (>=0.13.3)
* Cython (>=0.27.3)
* cvxopt (>=1.2.0) [optional: lovasz]
* future (>=0.16.0) (for python 2.7)


Installing Dependencies
-----------------------

You can install the dependencies as follows:

```shell
$ pip install extension>=extension_version
```

or

```shell
$ pip install -r requirements.txt
```

Installing the *development-version*
------------------------------------

To install the *development-version* using [**pip**](https://pypi.org/project/grakel-dev) execute:

```shell
$ pip install grakel-dev
```

Getting Started
===============
Two pointers to get you started:


Testing
=======
You first need to build the package's c++ extensions
locally by executing:
```shell
$ python setup.py build_ext -i
```

To test the package, execute:
```shell
$ nosetests
```

For executing unit_tests or use a testing-interface for testing the `kernel` module:
```shell
$ python  grakel/tests/test_kernels.py --help
usage: test_kernels.py [-h] [--verbose] [--problematic] [--slow]
                       [--ignore_warnings] [--dataset DATASET] [--normalize]
                       [--develop | --all | --main]

A test file for all kernels

optional arguments:
  -h, --help         show this help message and exit
  --verbose          print kernels with their outputs on stdout
  --problematic      allow execution of problematic test cases in development
  --slow             allow execution of slow test cases in development
  --ignore_warnings  ignore warnings produced by kernel executions
  --dataset DATASET  chose the datset you want the tests to be executed
  --normalize        normalize the kernel output
  --develop          execute only tests connected with current development
  --all              execute all tests
  --main             execute the main tests [default]

```

For testing `graph_kernels`:
```shell
$ python grakel/tests/test_graph_kernel.py --help
usage: test_graph_kernels.py [-h] [--verbose] [--problematic] [--slow]
                             [--normalize] [--ignore_warnings]
                             [--dataset DATASET] [--develop | --all | --main]

A test file for all kernels

optional arguments:
  -h, --help         show this help message and exit
  --verbose          print kernels with their outputs on stdout
  --problematic      allow execution of problematic test cases in development
  --slow             allow execution of slow test cases in development
  --normalize        normalize the kernel output
  --ignore_warnings  ignore warnings produced by kernel executions
  --dataset DATASET  chose the datset you want the tests to be executed
  --develop          execute only tests connected with current development
  --all              execute all tests
  --main             execute the main tests [default]

```

And for testing the `Graph` class:
```shell
$ python grakel/tests/test_graph.py --help
usage: test_graph.py [-h] [--verbose] [--ignore_warnings]

A test file for all `Graph` type objects

optional arguments:
  -h, --help         show this help message and exit
  --verbose          verbose outputs on stdout
  --ignore_warnings  ignore warnings produced by kernel executions
```
You can also execute the kernel test locally through a *test-main-function* as

```shell
$ python -m grakel.tests
```

Contributing
============
To learn how to integrate your own kernel and how to contribute to the GraKeL project, please read the sections *Write your own kernel* and *Contributing* in the [Documentation][doc], respectively.

[doc]: https://ysig.github.io/GraKeL/dev/
[examples]: https://ysig.github.io/GraKeL/dev/auto_examples/index.html

License
=======
GraKeL comes with a __BSD 3-clause__ license (as with scikit-learn).
It contains the C++ source code of [BLISS](http://www.tcs.hut.fi/Software/bliss) (a library for graph isomorphism) which is __LGPL__ licensed.
Futhermore its optional dependency in the package of [cvxopt](https://cvxopt.org/) (a tool for solving convex-optimization problems) comes with a __GPL__ license.

Citation
========
If you use GraKeL in a scientific publication, please cite our paper:

```
@article{siglidis2018grakel,
  title={GraKeL: A Graph Kernel Library in Python},
  author={Siglidis, Giannis and Nikolentzos, Giannis and Limnios, Stratis and Giatsidis, Christos and Skianis, Konstantinos and Vazirgiannis, Michalis},
  journal={arXiv preprint arXiv:1806.02193},
  year={2018}
}
```
