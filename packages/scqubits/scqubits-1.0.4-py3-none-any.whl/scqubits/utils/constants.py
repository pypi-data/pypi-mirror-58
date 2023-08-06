# constants.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

from enum import Enum, unique

import numpy as np

# file name suffices
PARAMETER_FILESUFFIX = '.prm'


# file types
@unique
class FileType(Enum):
    """Specifies the available file types for writing data to disk."""
    csv = 0
    h5 = 1


# helper functions for plotting wave functions
MODE_FUNC_DICT = {'abs_sqr': (lambda x: np.abs(x)**2),
                  'abs': (lambda x: np.abs(x)),
                  'real': (lambda x: np.real(x)),
                  'imag': (lambda x: np.imag(x))}


# enumerate variables for zero-pi qubit
PHI_INDEX = 0
THETA_INDEX = 1
ZETA_INDEX = 2
