# NIRFSOC-Simulation
Simulation of a near infrared free space optical communication system.

## Built With
This project was made with `Python 3.7.4`
The following packages were used:
* `matplotlib`
* `scipy`
* `numpy`
* `tkinter`

## How to Get Started Using This Application?
- The `GaussianBeam.py` file contains the class used to simulate a Gaussian beam.
  Read the comments to understand the class methods.
- The `intensityPlot.py` file is a GUI application for plotting intensity of Gaussian
  beams, importing the `GaussianBeam.py` file. The parameter inputs are self explanatory,
  but more information can be found in the comments.
- The `lensSystem.py` file is a GUI application for modelling Gaussian Beams through
  a thin lens system, importing the `GaussianBeam.py` file. The parameter inputs are 
  self explanatory, but more information can be found in the comments.
- To add more functionality, add more methods to the `GaussianBeam.py` class. To
  create a simulation, import the file and utilize the class and its methods.
