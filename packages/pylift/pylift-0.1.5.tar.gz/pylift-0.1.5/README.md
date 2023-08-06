# pylift

[![Documentation Status](https://readthedocs.org/projects/pylift/badge/?version=latest)](https://pylift.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.com/rsyi/pylift.svg?branch=master)](https://travis-ci.com/rsyi/pylift) [![GitHub version](https://badge.fury.io/gh/pylift%2Fpylift.svg)](https://badge.fury.io/gh/pylift%2Fpylift)

[Read our documentation!](https://pylift.readthedocs.io/en/latest/)

**pylift** is an uplift library that provides, primarily, (1) fast uplift modeling implementations and (2) evaluation tools (`UpliftEval` class). While other packages and more exact methods exist to model uplift, **pylift** is designed to be quick, flexible, and effective. **pylift** heavily leverages the optimizations of other packages -- namely, `xgboost`, `sklearn`, `pandas`, `matplotlib`, `numpy`, and `scipy`. The primary method currently implemented is the Transformed Outcome proxy method (Athey 2015).

This branch is a fork from [github.com/wayfair/pylift](https://github.com/wayfair/pylift), and is actively being maintained.

## Installation
This version of pylift can be installed through pypi:

```
pip install pylift
```

## License
Licensed under the BSD-2-Clause by the authors.

## Reference
Athey, S., & Imbens, G. W. (2015). Machine learning methods for estimating heterogeneous causal effects. stat, 1050(5).

Gutierrez, P., & Gérardy, J. Y. (2017). Causal Inference and Uplift Modelling: A Review of the Literature. In International Conference on Predictive Applications and APIs (pp. 1-13).

Hitsch, G., & Misra, S. (2018). Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation. Preprint
