import numpy as np

class Generator:  
  def __init__(self, model, latent_dims):
    self.latent_dims = latent_dims
    self.model = model

  def generate_latent_points(self,n):
    X = np.random.randn(self.latent_dims * n)
    X = X.reshape(n, self.latent_dims)
    return X

  def generate(self, n):
    X_input = self.generate_latent_points(n)
    X = self.model.predict(X_input)
    Y = np.zeros((n,1))
    return X, Y
