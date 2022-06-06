import numpy as np

def arr_product(arr: np.ndarray) -> int:
    """
    Returns the product of all numbers in the array
    Args:
        arr: np.ndarray
    Returns:
        int: product of all numbers
    """
    p = 1
    h,w = arr.shape
    for i in range(h):
        for j in range(w):
            p *= arr[i,j]
    return p

arr = np.array([1, 9, 4, 3, 5, 12, 3, 12, 3]).reshape(3, 3)
print(arr_product(arr))
print(np.prod(arr))