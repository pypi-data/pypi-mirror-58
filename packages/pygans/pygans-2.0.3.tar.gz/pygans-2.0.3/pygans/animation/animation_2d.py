from pygans.animation import Animation
import numpy as np

class Animation_2D(Animation):
  def __init__(self, plots, lower_limit, upper_limit, labels=None):
    super().__init__(plots)
    self.lower_limit = lower_limit
    self.upper_limit = upper_limit
    # Transforms Probabilities in Colours
    self.labels = labels*100
    self.ax.set(xlim=(lower_limit,upper_limit))
    self.scat = self.ax.scatter([], [])

  def update(self, i):
    if self.labels != None:
      labels = self.labels[i]
      labels = labels.reshape(labels.shape[0])
      self.scat.set_array(labels)
    self.scat.set_offsets(self.plots[i])
    return self.scat,

  def draw_function(self,function):
    increment = 0.0001
    ll = self.lower_limit
    ul = self.upper_limit
    X = list(np.arange(ll,ul,increment))
    Y = [function(i) for i in X]
    self.ax.plot(X,Y)

