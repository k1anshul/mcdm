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
Test module for the ``weighting/critic_method.py`` file of the ``mcdm``
package.
"""

import unittest

import numpy as np

from mcdm.weighting import critic


class TestCritic(unittest.TestCase):
    """
    Test class for the ``critic`` function of the ``mcdm.weighting`` package.
    """
    def test_linear(self):
        """
        Test the CRITIC weighting method with a linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix)
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_nonlinear(self):
        """
        Test the CRITIC weighting method with a non-linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.2, 0.5, 0.0],
                [0.2, 0.5, 1.0],
                [0.4, 1.0, 0.0],
                [0.4, 1.0, 1.0],
                [0.6, 1.0, 0.0],
                [0.6, 1.0, 1.0],
                [0.8, 0.5, 0.0],
                [0.8, 0.5, 1.0],
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 1.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix)
        expected_w_vector = np.array(
            [0.27329284, 0.32664742, 0.40005975],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_float32(self):
        """
        Test the CRITIC weighting method with a float32 NumPy array.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float32,
        )
        obtained_w_vector = critic(z_matrix)
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_nested_list(self):
        """
        Test the CRITIC weighting method with a nested list.
        """
        z_matrix = [
            [0.0, 0.0, 1.0],
            [0.1, 0.2, 0.8],
            [0.2, 0.4, 0.6],
            [0.3, 0.7, 0.3],
            [0.6, 0.8, 0.2],
            [0.8, 0.9, 0.1],
            [1.0, 1.0, 0.0],
        ]
        obtained_w_vector = critic(z_matrix)
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_pearson_linear(self):
        """
        Test the CRITIC.Pearson weighting method with a linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "Pearson")
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_pearson_nonlinear(self):
        """
        Test the CRITIC.Pearson weighting method with a non-linear
        association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.2, 0.5, 0.0],
                [0.2, 0.5, 1.0],
                [0.4, 1.0, 0.0],
                [0.4, 1.0, 1.0],
                [0.6, 1.0, 0.0],
                [0.6, 1.0, 1.0],
                [0.8, 0.5, 0.0],
                [0.8, 0.5, 1.0],
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 1.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "Pearson")
        expected_w_vector = np.array(
            [0.27329284, 0.32664742, 0.40005975],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_pearson_float32(self):
        """
        Test the CRITIC.Pearson weighting method with a float32 NumPy array.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float32,
        )
        obtained_w_vector = critic(z_matrix, "Pearson")
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_pearson_nested_list(self):
        """
        Test the CRITIC.Pearson weighting method with a nested list.
        """
        z_matrix = [
            [0.0, 0.0, 1.0],
            [0.1, 0.2, 0.8],
            [0.2, 0.4, 0.6],
            [0.3, 0.7, 0.3],
            [0.6, 0.8, 0.2],
            [0.8, 0.9, 0.1],
            [1.0, 1.0, 0.0],
        ]
        obtained_w_vector = critic(z_matrix, "Pearson")
        expected_w_vector = np.array(
            [0.25000000, 0.25857023, 0.49142977],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_abspearson_linear(self):
        """
        Test the CRITIC.AbsPearson weighting method with a linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "AbsPearson")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_abspearson_nonlinear(self):
        """
        Test the CRITIC.AbsPearson weighting method with a non-linear
        association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.2, 0.5, 0.0],
                [0.2, 0.5, 1.0],
                [0.4, 1.0, 0.0],
                [0.4, 1.0, 1.0],
                [0.6, 1.0, 0.0],
                [0.6, 1.0, 1.0],
                [0.8, 0.5, 0.0],
                [0.8, 0.5, 1.0],
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 1.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "AbsPearson")
        expected_w_vector = np.array(
            [0.27329284, 0.32664742, 0.40005975],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_abspearson_float32(self):
        """
        Test the CRITIC.AbsPearson weighting method with a float32 NumPy
        array.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float32,
        )
        obtained_w_vector = critic(z_matrix, "AbsPearson")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_abspearson_nested_list(self):
        """
        Test the CRITIC.AbsPearson weighting method with a nested list.
        """
        z_matrix = [
            [0.0, 0.0, 1.0],
            [0.1, 0.2, 0.8],
            [0.2, 0.4, 0.6],
            [0.3, 0.7, 0.3],
            [0.6, 0.8, 0.2],
            [0.8, 0.9, 0.1],
            [1.0, 1.0, 0.0],
        ]
        obtained_w_vector = critic(z_matrix, "AbsPearson")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_dcor_linear(self):
        """
        Test the CRITIC.dCor weighting method with a linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "dCor")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_dcor_nonlinear(self):
        """
        Test the CRITIC.dCor weighting method with a non-linear association.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.2, 0.5, 0.0],
                [0.2, 0.5, 1.0],
                [0.4, 1.0, 0.0],
                [0.4, 1.0, 1.0],
                [0.6, 1.0, 0.0],
                [0.6, 1.0, 1.0],
                [0.8, 0.5, 0.0],
                [0.8, 0.5, 1.0],
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 1.0],
            ],
            dtype=np.float64,
        )
        obtained_w_vector = critic(z_matrix, "dCor")
        expected_w_vector = np.array(
            [0.23971980, 0.28651997, 0.47376023],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_dcor_float32(self):
        """
        Test the CRITIC.dCor weighting method with a float32 NumPy array.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float32,
        )
        obtained_w_vector = critic(z_matrix, "dCor")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_dcor_nested_list(self):
        """
        Test the CRITIC.dCor weighting method with a nested list.
        """
        z_matrix = [
            [0.0, 0.0, 1.0],
            [0.1, 0.2, 0.8],
            [0.2, 0.4, 0.6],
            [0.3, 0.7, 0.3],
            [0.6, 0.8, 0.2],
            [0.8, 0.9, 0.1],
            [1.0, 1.0, 0.0],
        ]
        obtained_w_vector = critic(z_matrix, "dCor")
        expected_w_vector = np.array(
            [0.50000000, 0.25000000, 0.25000000],
            dtype=np.float64,
        )
        np.testing.assert_allclose(obtained_w_vector, expected_w_vector)
        self.assertEqual(obtained_w_vector.dtype, expected_w_vector.dtype)

    def test_missing_element_exception(self):
        """
        Test the CRITIC weighting method with a missing element.
        """
        z_matrix = [
            [0.0, 0.0, 1.0],
            [0.1, 0.2, 0.8],
            [0.2, 0.4, 0.6],
            [0.3, 0.7, 0.3],
            [0.6, 0.8, 0.2],
            [0.8, 0.9],
            [1.0, 1.0, 0.0],
        ]
        self.assertRaises(ValueError, critic, z_matrix)

    def test_over_exception(self):
        """
        Test the CRITIC weighting method with a value greater than one.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.1],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        self.assertRaises(ValueError, critic, z_matrix)

    def test_under_exception(self):
        """
        Test the CRITIC weighting method with a value less than zero.
        """
        z_matrix = np.array(
            [
                [ 0.0, 0.0, 1.0],  # noqa: E201
                [-0.1, 0.2, 0.8],  # noqa: E201
                [ 0.2, 0.4, 0.6],  # noqa: E201
                [ 0.3, 0.7, 0.3],  # noqa: E201
                [ 0.6, 0.8, 0.2],  # noqa: E201
                [ 0.8, 0.9, 0.1],  # noqa: E201
                [ 1.0, 1.0, 0.0],  # noqa: E201
            ],
            dtype=np.float64,
        )
        self.assertRaises(ValueError, critic, z_matrix)

    def test_unknown_selection_exception(self):
        """
        Test the CRITIC weighting method with an unknown correlation method.
        """
        z_matrix = np.array(
            [
                [0.0, 0.0, 1.0],
                [0.1, 0.2, 0.8],
                [0.2, 0.4, 0.6],
                [0.3, 0.7, 0.3],
                [0.6, 0.8, 0.2],
                [0.8, 0.9, 0.1],
                [1.0, 1.0, 0.0],
            ],
            dtype=np.float64,
        )
        self.assertRaises(ValueError, critic, z_matrix, "Unknown")


if __name__ == "__main__":
    unittest.main()
