import numpy as np

def sum_axis_1(arr: np.ndarray) -> int:
    """
    Returns the sum of rows in the array
    Args:
        arr: np.ndarray
    Returns:
        np.ndarray: sum of each row
    """
    return np.sum(arr, axis=1)