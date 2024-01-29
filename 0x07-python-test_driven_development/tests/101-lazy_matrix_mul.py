#!/usr/bin/python3
import numpy as np
"""
module function that multiplies 2 matrices by using the module NumPy
Test cases should be the same as 100-matrix_mul but
with new exception type/message
"""


def lazy_matrix_mul(m_a, m_b):
    """
     Args: : m_a (list of lists), m_b (list of lists)
    """

    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)
    try:
        np_m_a.astype(np.float64)
        np_m_b.astype(np.float64)
    except ValueError:
        raise TypeError("m_a and m_b should contain only integers or floats")

    if np_m_a.size == 0 or np_m_b.size == 0:
        raise ValueError("m_a and m_b can't be empty")
    if np_m_a.shape[1] != np_m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    # Perform matrix multiplication using NumPy
    result_matrix = np.dot(np_m_a, np_m_b)
    # convert to list
    return np.array_str(result_matrix)
