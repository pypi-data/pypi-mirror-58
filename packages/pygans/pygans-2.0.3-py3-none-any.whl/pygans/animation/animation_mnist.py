import math
from pygans.animation import Animation
import matplotlib.pyplot as plt

class Animation_MNIST(Animation):
  def __init__(self, plots, dims=None):
    super().__init__(plots)
    if dims == None:
      size = int(math.sqrt(len(plots[0])))
      dims = (size,size)
    self.rows, self.cols = dims

  def update(self, i):
    X = self.plots[i]
    r, c = self.rows, self.cols
    n = r * c
    for i in range(n):
      plt.subplot(r, c, 1 + i)
      plt.axis('off')
      plt.imshow(X[i, :, :, 0], cmap='gray_r')
