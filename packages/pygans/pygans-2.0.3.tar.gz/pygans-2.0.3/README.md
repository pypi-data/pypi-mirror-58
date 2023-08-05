# PyGANs (Machine Learning Framework)

Python Framework for Generative Adversarial Networks. It provides an Abstraction layer to create and train GANs with an integrated monitoring module to see the evolution of the Network through time.

There are incorporated examples that show the usage of the framework in 2D functions and generating Hand Written Digits.

Tested Models:
* Trigonometric Functions (f(x)=sin(x))  
*  Polynomial Functions, for example:  
O f(x) = x\*\*2  
O f(x) = x\*\*5 - 3x\*\*2 - 4  
* HandWritten Digits (MNIST)

## Installation

PyGANs is available in the Python Package Index (PyPI), so it's possible to install it using the package installer for Python (pip), which install automatically the external dependencies:  

**$**  pip install pygans

## External Dependencies

If you install the library using **pip**, it will install automatically the dependencies.

* Keras
* Tensorflow
* Numpy
* Matplotlib

## Versions

**2.0.3**  

  BugFix: Random Generation in Dataset_Generator_2D  

**2.0.2**  

* BugFix: MNIST Animation  

**2.0.0**  

* MNIST Supported  
* Simplified API  
* Optimizing training process  
* BugFix: Latent points generation on Standard normal distribution  

**1.0.0**  

* 2D Functions tested  
* 2D animation supported  