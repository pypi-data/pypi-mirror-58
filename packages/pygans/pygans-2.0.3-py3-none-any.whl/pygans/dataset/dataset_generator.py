# Dataset Generator
from abc import ABC, abstractmethod
import numpy as np

class Dataset_Generator(ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def generate_real_samples(self,n):
    pass

  def generate_fake_samples(self, n, generator):
    X, Y = generator.generate(n)
    return X, Y

  def generate_dataset(self, n, generator):
    n_real = n//2
    n_fake = n//2
    if n % 2 != 0:
      n_real += 1
    x_real, y_real = self.generate_real_samples(n_real)
    X_fake, y_fake = self.generate_fake_samples(n_fake, generator)
    X, Y = np.vstack((x_real, X_fake)), np.vstack((y_real, y_fake))
    return X,Y





  
