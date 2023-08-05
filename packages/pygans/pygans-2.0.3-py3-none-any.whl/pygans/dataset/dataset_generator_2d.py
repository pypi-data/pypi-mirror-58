from pygans.dataset import Dataset_Generator
import numpy as np

class Dataset_Generator_2D(Dataset_Generator):
  def __init__(self, function, lower_limit, upper_limit):
    super().__init__()
    self.lower_limit = lower_limit
    self.upper_limit = upper_limit
    self.width = upper_limit - lower_limit
    self.function = function

  def generate_real_samples(self,n):
    X_generated = self.width * np.random.randn(n) + self.lower_limit
    Y_generated = [ self.function(i) for i in X_generated ]
    X = np.asarray(X_generated).reshape(n, 1)
    Y = np.asarray(Y_generated).reshape(n, 1)
    samples = np.hstack((X, Y))
    labels = np.ones((n,1))
    return samples, labels