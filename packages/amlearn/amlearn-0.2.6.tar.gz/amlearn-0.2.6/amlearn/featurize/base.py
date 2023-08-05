import os
import time
from functools import lru_cache

import six
import json
import numpy as np
from amlearn.utils.backend import BackendContext, FeatureBackend
from sklearn.base import BaseEstimator, TransformerMixin
from abc import ABCMeta, abstractmethod


try:
    from amlearn.featurize.src \
        import voronoi_stats
except Exception:
    print("import fortran file voronoi_stats error!\n")

module_dir = os.path.dirname(os.path.abspath( __file__))

__author__ = "Qi Wang"
__email__ = "qiwang.mse@gmail.com"


@lru_cache(maxsize=5)
def create_featurizer_backend(output_path='tmp'):
    """Create default featurizer backend.

    Returns:
        featurizer_backend (object): Featurizer Backend.
    """
    output_path = 'tmp' if output_path is None or output_path == 'tmp' \
        else output_path
    backend_context = BackendContext(merge_path=True,
                                     output_path=output_path)
    featurizer_backend = FeatureBackend(backend_context)
    return featurizer_backend


def line_percent(value_list):
    percent_list = np.zeros(value_list.shape)

    percent_list = \
        voronoi_stats.line_percent(percent_list, value_list)
    return percent_list


class BaseFeaturize(six.with_metaclass(ABCMeta,
                                       BaseEstimator, TransformerMixin)):
    """Base featurize class for amlearn.

    Args:
        save (Boolean): save file or not.
        backend (Backend): Amlearn Backend object, to prepare amlearn needed
            paths and define the common amlearn's load/save method.
    """

    def __init__(self, save=True, verbose=1, backend=None, output_path=None):
        self.save = save
        self.verbose = verbose
        if self.save:
            self.backend = backend if backend is not None \
                else create_featurizer_backend(output_path=output_path)
        self.dependent_class_ = None
        self.dependent_cols_ = None

    def transform(self, X):
        pass

    @abstractmethod
    def get_feature_names(self):
        pass

    @property
    def dependent_class(self):
        return self.dependent_class_

    @property
    def category(self):
        return 'sro'

    def check_dependency(self, X):
        if self.dependent_class_ is None:
            dependent_class = None
        elif set(self.dependent_cols_).issubset(set(X.columns)):
            dependent_class = None
        else:
            dependent_class = self.dependent_class_
        return dependent_class

