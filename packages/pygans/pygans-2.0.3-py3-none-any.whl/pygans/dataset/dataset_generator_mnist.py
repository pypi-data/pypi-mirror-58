from pygans.dataset import Dataset_Generator
import numpy as np

# Dataset Generator MNIST
from keras.datasets import mnist

class Dataset_Generator_MNIST(Dataset_Generator):
  def __init__(self):
    super().__init__()
    self.real_samples = self.load_real_samples()

  def load_real_samples(self):
    (trainX, _), (_, _) = mnist.load_data()
    X = np.expand_dims(trainX, axis=-1)
    X = X.astype('float32')
    X = X / 255.0
    return X

  def generate_real_samples(self, n):
    ix = np.random.randint(0, self.real_samples.shape[0], n)
    X = self.real_samples[ix]
    Y = np.ones((n, 1))
    return X, Y
