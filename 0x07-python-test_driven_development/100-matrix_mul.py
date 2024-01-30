def matrix_mul(m_a, m_b):
    """
    Args:- m_a (list of lists), m_b (list of lists)
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not isinstance(element, (int, float))
           for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    length_row = len(m_a[0])
    for x in range(len(m_a)):
        if len(m_a[x]) != length_row:
            raise TypeError("each row of m_a must be of the same size")
    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(element, (int, float))
           for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    length_row = len(m_b[0])
    for x in range(len(m_b)):
        if len(m_b[x]) != length_row:
            raise TypeError("each row of m_b must be of the same size")
    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Perform matrix multiplication
    result_matrix = [
        [sum(a * b for a, b in zip(row_a, col_b))
         for col_b in zip(*m_b)] for row_a in m_a
         ]

    return result_matrix
