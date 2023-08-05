from keras.models import Sequential
import numpy as np

class GAN:
  def create_model(self, loss="binary_crossentropy", optimizer="adam"):
    discriminator_model = self.discriminator.model
    discriminator_model.trainable = False
    model = Sequential()
    model.add(self.generator.model)
    model.add(discriminator_model)
    model.compile(loss=loss, optimizer=optimizer)
    return model

  def __init__(self, discriminator, generator, optimizer="adam"):
    self.discriminator = discriminator
    self.generator = generator
    self.model = self.create_model(optimizer=optimizer)

  def train_on_batch(self, batch_size):
    x = self.generator.generate_latent_points(batch_size)
    y = np.ones((batch_size,1))
    loss = self.model.train_on_batch(x, y)
    return loss

  def train(self, dataset_generator, iterations, batch_size, verbose=0, freq_generation=0, n_generations=100):
    generations = []
    discriminations = []
    for i in range(1,iterations+1):
      x, y = dataset_generator.generate_dataset(batch_size, self.generator)
      d_loss = self.discriminator.train_on_batch(x, y)
      g_loss = self.train_on_batch(batch_size)
      if verbose:
          print("Iteration:",i,d_loss,g_loss)
      if freq_generation != 0 and (i % freq_generation == 0 or i == 0):
        if verbose == 0:
          print("Iteration ",i)
        g,_ = self.generator.generate(n_generations)
        d = self.discriminator.predict(g)
        generations.append(g)
        discriminations.append(d)
    return generations, discriminations

  def evaluate(self, validation_data, n_fake_samples=100):
    x_test_discriminator, y_test_discriminator = validation_data
    x_fake, y_fake = self.generator.generate(n_fake_samples)
    
    _, acc_disc = self.discriminator.evaluate(x_test_discriminator, y_test_discriminator)
    _, acc_fake_samples = self.discriminator.evaluate(x_fake, y_fake)
  
    print("Accuracy Discriminator:",acc_disc*100//1,"%")
    print("Percentage of Fake Samples detected:",acc_fake_samples*100//1,"%")
