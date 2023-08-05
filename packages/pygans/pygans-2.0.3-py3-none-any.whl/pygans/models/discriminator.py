class Discriminator:
  def __init__(self, model):
    self.model = model

  def fit(self, x, y, epochs, batch_size, validation_data = None, verbose=0):
    history = self.model.fit(x, y, epochs=epochs, batch_size=batch_size, verbose=verbose, validation_data = validation_data)
    return history

  def train_on_batch(self, x, y, verbose=0):
    loss = self.model.train_on_batch(x, y)
    return loss

  def evaluate(self, x, y, verbose=0):
    return self.model.evaluate(x,y, verbose=verbose)

  def predict(self, inputs, verbose=0):
    return self.model.predict(inputs, verbose=verbose)
