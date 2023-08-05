from matplotlib import animation, rc
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Animation(ABC):
  def __init__(self,plots):
    super().__init__()
    self.plots = plots
    fig, ax = plt.subplots()
    self.fig = fig
    self.ax = ax

  @abstractmethod
  def update(self,i):
    pass

  def get_animation(self, fps):
    interval = 1000 / fps
    frames = len(self.plots)
    an = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=interval)
    return an
  
  def save(self, anim, fps, path, filename="animation", writer="imagemagick"):
    full_path = path + "/" + filename + ".gif"
    anim.save(full_path, writer=writer, fps=fps)
