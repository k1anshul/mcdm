#!/usr/bin/env python3

# Copyright (c) 2020-2021 Dimitrios-Georgios Akestoridis
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Test module for the ``helper_scoring.py`` file of the ``mcdm`` package.
"""

import unittest

import numpy as np

from mcdm import score


class TestScore(unittest.TestCase):
    """
    Test class for the ``score`` function of the ``mcdm`` package.
    """
    def test_unknown_selection_exception(self):
        """
        Test the selection of an unknown scoring method.
        """
        z_matrix = np.array(
            [
                [0.00, 1.00],
                [0.25, 0.75],
                [0.50, 0.50],
                [0.75, 0.25],
                [1.00, 0.00],
            ],
            dtype=np.float64,
        )
        is_benefit_z = [True, True]
        w_vector = np.array([0.5, 0.5], dtype=np.float64)
        self.assertRaises(
            ValueError,
            score,
            z_matrix,
            is_benefit_z,
            w_vector,
            "Unknown",
        )


if __name__ == "__main__":
    unittest.main()
