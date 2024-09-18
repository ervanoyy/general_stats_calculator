import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError()

  matrix = np.reshape(list, (3, 3))

  calculations = {
      'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean()],
      'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var()],

      'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std()],
      'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(),
 matrix.flatten().max()],
      'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min()],
      'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

  }

  return calculations
#
#
# # Example usage
# text = input("Enter the elements separated by spaces: ")
# list = [int(x) for x in text.split()]
# result = calculate(list)
# print(result)