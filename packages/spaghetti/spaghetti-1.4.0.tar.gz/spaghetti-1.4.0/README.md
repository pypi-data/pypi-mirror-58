
[pysal/spaghetti](http://pysal.org/spaghetti/)
=========================================================

SPAtial GrapHs: nETworks, Topology, & Inference
===============================================

*An example of snapping observation points to a network and plotting:*
<p align="center">
<img src="figs/snap_plot.png" width="650" height="450" />
</p>

|[![PyPI version](https://badge.fury.io/py/spaghetti.svg)](https://badge.fury.io/py/spaghetti)| [![Conda Version](https://img.shields.io/conda/vn/conda-forge/spaghetti.svg)](https://anaconda.org/conda-forge/spaghetti) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/spaghetti.svg)](https://anaconda.org/conda-forge/spaghetti) | [![Gitter](https://badges.gitter.im/pysal/Spaghetti.svg)](https://gitter.im/pysal/Spaghetti?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
|:---:|:---:|:---:|:---:|
|[![Build Status](https://travis-ci.org/pysal/spaghetti.svg?branch=master)](https://travis-ci.org/pysal/spaghetti) | [![Documentation](https://img.shields.io/static/v1.svg?label=docs&message=current&color=9cf)](http://pysal.org/spaghetti/) | [![Coverage Status](https://coveralls.io/repos/github/pysal/spaghetti/badge.svg)](https://coveralls.io/github/pysal/spaghetti) | [![Conda Recipe](https://img.shields.io/badge/recipe-spaghetti-green.svg)](https://github.com/conda-forge/spaghetti-feedstock)
|[![GitHub issues open](https://img.shields.io/github/issues/pysal/spaghetti.svg?maxAge=3600)](https://github.com/pysal/spaghetti/issues) | ![Github pull requests open](https://img.shields.io/github/issues-pr/pysal/spaghetti.svg) | ![Pypi python versions](https://img.shields.io/pypi/pyversions/spaghetti.svg) | [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
|[![GitHub issues closed](https://img.shields.io/github/issues-closed/pysal/spaghetti.svg?maxAge=3600)](https://github.com/pysal/spaghetti/issues) | ![Github pull requests closed](https://img.shields.io/github/issues-pr-closed/pysal/spaghetti.svg) | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) | [![DOI](https://zenodo.org/badge/88305306.svg)](https://zenodo.org/badge/latestdoi/88305306)

--------------------------------------

This package is part of a [refactoring of PySAL](https://github.com/pysal/pysal/wiki/PEP-13:-Refactor-PySAL-Using-Submodules).

--------------------------------------

Spaghetti is an open-source Python library for the analysis of network-based spatial data. Originating from the `network` module in [PySAL (Python Spatial Analysis Library)](http://pysal.org), it is under active development for the inclusion of newly proposed methods for building graph-theoretic networks and the analysis of network events.

-------------------------------


Examples
--------
* [Network Representation](https://pysal.org/spaghetti/notebooks/Basic_spaghetti_tutorial.html)
* [Spatial Network Analysis](https://pysal.org/spaghetti/notebooks/Advanced_spaghetti_tutorial.html)
* [Optimal Facility Location](https://pysal.org/spaghetti/notebooks/Use_case-facility_location.html)


Installation
------------

As of version 1.3, `spaghetti` officially supports Python [`3.6`](https://docs.python.org/3.6/) and [`3.7`](https://docs.python.org/3.7/) only. Please make sure that you are operating in a Python 3 environment.

**Installing with `conda` via [conda-forge](https://github.com/conda-forge/spaghetti-feedstock) (highly recommended)**

To install `spaghetti` and all its dependencies, we recommend using the [`conda`](https://docs.conda.io/en/latest/)
manager, specifically with the [`conda-forge`](https://conda-forge.org) channel. This can be obtained by installing the [`Anaconda Distribution`](https://docs.continuum.io/anaconda/) (a free Python distribution for data science), or through [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) (minimal distribution only containing Python and the conda package manager). 

Using `conda`, `spaghetti` can be installed as follows:
```
$ conda config --set channel_priority strict
$ conda install --channel conda-forge spaghetti
```

**Installing with [`PyPI`](https://pypi.org/project/spaghetti/)**
```
$ pip install spaghetti
```
*or* download the source distribution (`.tar.gz`) and decompress it to your selected destination. Open a command shell and navigate to the decompressed folder.
```
$ pip install .
```

***Warning***

When installing via `pip`, you have to ensure that the required dependencies for `spaghetti` are installed on your operating system. Details on how to install these packages are linked below. Using `conda` (above) avoids having to install the dependencies separately.

Install the most current development version of `spaghetti` by running:

```
$ pip install git+https://github.com/pysal/spaghetti
```


Requirements
------------
- [`esda`](https://esda.readthedocs.io/en/latest/)
- [`libspatialindex`](https://libspatialindex.org/index.html)
- [`numpy`](https://numpy.org/devdocs/)
- [`rtree`](http://toblerity.org/rtree/install.html)
- [`scipy`](http://scipy.github.io/devdocs/)

Soft Dependencies
-----------------
- [`geopandas`](http://geopandas.org/install.html)
- [`shapely`](https://shapely.readthedocs.io/en/latest/)

Contribute
----------

PySAL-spaghetti is under active development and contributors are welcome.

If you have any suggestion, feature request, or bug report, please open a new [issue](https://github.com/pysal/spaghetti/issues) on GitHub. To submit patches, please follow the PySAL development [guidelines](https://github.com/pysal/pysal/wiki) and open a [pull request](https://github.com/pysal/spaghetti). Once your changes get merged, you’ll automatically be added to the [Contributors List](https://github.com/pysal/spaghetti/graphs/contributors).

Support
-------

If you are having issues, please [create an issue](https://github.com/pysal/spaghetti/issues) or talk to us in the [gitter room](https://gitter.im/pysal/spaghetti).

License
-------

The project is licensed under the [BSD license](https://github.com/pysal/spaghetti/blob/master/LICENSE.txt).

BibTeX Citation
---------------

```
@misc{Gaboardi2018,
    author    = {Gaboardi, James D. and Laura, Jay and Rey, Sergio and Wolf, Levi John and Folch, David C. and Kang, Wei and Stephens, Philip and Schmidt, Charles},
    month     = {oct},
    year      = {2018},
    title     = {pysal/spaghetti},
    url       = {https://github.com/pysal/spaghetti},
    doi       = {10.5281/zenodo.1343650},
    keywords  = {graph-theory,network-analysis,python,spatial-networks,topology}
}
```


