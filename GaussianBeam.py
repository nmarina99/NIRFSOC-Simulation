'''
A class for simulating Gaussian Beams
Utilizes the numpy and matplotlib packages
Created On: 10/23/19
Created By: Nicholas Marina
Last Updated: 10/25/19
'''

import numpy as np
from matplotlib import pyplot as plt

class GaussianBeam:
    def __init__(self, wavelength, power, divergence):
        '''Initializes a GaussianBeam object
        param wavelength: wavelength of the laser (in meters)
        param power: power of the laser (in watts)
        param divergence: divergence angle of the laser (in degrees)'''
        self.power = power
        self.divergence = divergence
        self.wavelength = wavelength
        # waist, z0, and I are the beam waist, Rayleigh length, and initial center intensity of the beam
        self.waist = wavelength/(np.pi*np.tan(np.radians(divergence)))
        self.z0 = (self.waist**2)*(np.pi/wavelength)
        self.I = 2*power/(np.pi*self.waist)
    def intensity_2d(self, z):
        '''Returns the intensity (in W/m^2) of the Gaussian beam in the plane distance z away from the waist
        param z: distance from the beam waist (in meters)'''
        # W and zeta are parameters used in the intensity calculations
        W = self.waist*np.sqrt(1 + (z/self.z0)**2)
        zeta = np.arctan(z/self.z0)
        def intensity(rho):
            '''Returns the intensity (in W/m^2) of the Gaussian beam distance rho away from the center
            param rho: distance from the center of the beam (in meters)'''
            k = 2*np.pi/self.wavelength
            U = self.I*((self.waist/W)**2)*np.exp(-2*(rho**2)/(W**2))
            return U
        # Returns the intensity function for the plane
        return intensity
    def radial_intensity(self, zL, N=100):
        '''Plots the intensity (in W/m^2) as a function of distance from the center of the beam at distance z from the waist
        param zL: distance from the beam waist (in meters)
        param N: the number of points to sample for (defaults to 100)'''
        W = self.waist*np.sqrt(1 + (max(zL)/self.z0)**2)
        # linspace object is an array of values to sample (acts like a vector)
        r = np.linspace(-2*W, 2*W, N)
        for z in zL:    
            I = np.vectorize(self.intensity_2d(z))(r)
            plt.plot(r, I)
        plt.show()
    def intensity_plot(self, z, xw = None , yw = None, NX = 100, NY = 100):
        '''Plots the intensity (in W/m^2) distance z away from the beam waist, over a rectangle of size xw*yw
        param z: distance from the beam waist (in meters)
        param xw, yw: horizontal and vertical width of the measurement area (in meters) - defaults to 2 times the beam width
        param NX, NY: number of x and y values to sample over (defaults to 100)'''
        W = self.waist*np.sqrt(1 + (z/self.z0)**2)
        # If no width is specified, 4 times the beam width is defaulted to
        if xw == None:
            xw = 4*W
        if yw == None:
            yw = 4*W
        x = np.linspace(-xw/2, xw/2, NX)
        y = np.linspace(-yw/2, yw/2, NY)
        # meshgrid object is a 2x2 matrix of points to sample
        X, Y = np.meshgrid(x, y)
        Z = np.vectorize(lambda x, y:self.intensity_2d(z)(np.sqrt(x**2 + y **2)))(X, Y)
        plt.imshow(Z, extent=[-xw*50, xw*50, -yw*50, yw*50], cmap='plasma')
        plt.title('Irradiance (W/m²) at ' + str(z) + ' m (' + str(self.wavelength*1e9) + ' nm, ' + str(self.power*1000) + ' mW, ' + str(self.divergence) + '° divergence)')
        plt.xlabel('x (cm)')
        plt.ylabel('y (cm)')
        plt.colorbar()
        plt.show()
    def max_intensity(self, z1, z2, N = 100):
        '''Plots the maximum intensity (in W/m^2) of the beam between distances z1 and z2 from the beam waist
        param z1, z1: starting and ending points to measure intensity over (in meters)
        param N: number of points to sample for (defaults to 100)'''
        z = np.linspace(z1, z2, N)
        I = np.vectorize(lambda z: self.I/(1 + (z/self.z0)**2))(z)
        plt.plot(z, I)
        plt.title('Maximum Irradiance (' + str(self.wavelength*1e9) + ' nm, ' + str(self.power*1000) + ' mW, ' + str(self.divergence) + '° divergence)')
        plt.ylabel('Irradiance (W/m²)')
        plt.xlabel('Distance (m)')
        plt.show()
    def width_plot(self, z1, z2, N = 100):
        '''Plots beam width (in cm) of the beam between distances z1 and z2 from the beam waist
        param z1, z1: starting and ending points to measure beam waist over (in meters)
        param N: number of points to sample for (defaults to 100)'''
        z = np.linspace(z1, z2, N)
        W = np.vectorize(lambda z: 100*self.waist*np.sqrt(1 + (z/self.z0)**2))(z)
        plt.plot(z, W)
        plt.ylim(ymin=0)
        plt.title('Beam Width (' + str(self.wavelength*1e9) + ' nm, ' + str(self.power*1000) + ' mW, ' + str(self.divergence) + '° divergence)')
        plt.ylabel('Beam Width Radius (cm)')
        plt.xlabel('Distance (m)')
        plt.show()

if __name__ == '__main__':
    # These are some tests; they will not execute if imported
    cheap = GaussianBeam(850e-9, 1.5e-3, 4)
    expensive = GaussianBeam(850e-9, 3e-3, 0.0344)
    cheap.waist_plot(0, 1, 100)
    expensive.waist_plot(0, 1, 100)
