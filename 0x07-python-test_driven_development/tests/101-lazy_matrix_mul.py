#!/usr/bin/python3
"""
Module : function that multiplies 2 matrices by using the module NumPy
m_a: first matrix
m_b: second_matrix
dsfd
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices by using the NumPy module.
    Args:
        (list of lists) m_a, (list of lists) m_b
    """

    return (np.matmul(m_a, m_b))
