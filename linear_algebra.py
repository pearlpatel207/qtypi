import numpy as np


def inner_product(vec1, vec2, show_steps=False):
  """
  Calculates the inner product of two vectors, optionally showing intermediate steps.

  Args:
      vec1: A numpy array representing the first vector.
      vec2: A numpy array representing the second vector.
      show_steps: Boolean flag indicating whether to show intermediate steps (default: False).

  Returns:
      A float representing the inner product of the two vectors.
  """
  if len(vec1) != len(vec2):
    raise ValueError("Vectors must have the same dimension.")

  if show_steps:
    print("Vector 1:", vec1)
    print("Conjugate transpose of Vector 2:")
    vec2_conj_transpose = vec2.conj().T
    print(vec2_conj_transpose)

  inner_product_result = np.sum(vec1 * vec2.conj())

  if show_steps:
    print("Element-wise product:")
    element_wise_product = vec1 * vec2.conj()
    print(element_wise_product)
    print("Sum of element-wise products:", inner_product_result)

  return inner_product_result
