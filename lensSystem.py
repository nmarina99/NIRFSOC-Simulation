
'''
A GUI for creating fast models for Gaussian beams through a thin lens system
Utilizes the tkinter, numpy, and matplotlib packages, and imports the GaussianBeam.py file
Created On: 10/30/19
Created By: Nicholas Marina
Last Updated: 10/30/19
'''

import tkinter as tk
import numpy as np
import GaussianBeam

# The window is initialized and the title and size are set
master = tk.Tk()
master.geometry('500x200')
master.title('Gaussian Beam Thin Lens System')

def update():
    # This function updates the labels to give the user the parameters
    if wavelength.get() and power.get() and div.get() and dist.get() and foc.get() and z.get():
        beam = GaussianBeam.GaussianBeam(float(wavelength.get())*1e-9, float(power.get())*1e-3, float(div.get()), 0)
        distances = list(map(float, dist.get().split(',')))
        focal_lengths = list(map(float, foc.get().split(',')))
        width = beam.thinLensFunction(distances, focal_lengths)(float(z.get()))
        for i in range(len(distances)):
            beam = beam.thinLens(distances[i], focal_lengths[i])
        angle = beam.divergence
        PR = beam.squareAperturePower(float(z.get()), float(xw.get())/100, float(yw.get())/100)
        W.set('Beam Diameter: ' + np.format_float_scientific(200*width, 3) + ' cm')
        theta.set('Beam Divergence: ' + np.format_float_scientific(angle, 3) + ' degrees')
        power_R.set('Power Recieved: ' + np.format_float_scientific(1000*PR, 3) + ' mW')

def width_plot():
    # This function creates a plot of the beam width through the lens system
    if wavelength.get() and power.get() and div.get() and dist.get() and foc.get() and z.get():
        beam = GaussianBeam.GaussianBeam(float(wavelength.get())*1e-9, float(power.get())*1e-3, float(div.get()), 0)
        distances = list(map(float, dist.get().split(',')))
        focal_lengths = list(map(float, foc.get().split(',')))
        beam.thinLensPlot(distances, focal_lengths, 0, float(z.get()))

def intensity_plot():
    # This function creates a plot of the intensity at the specified distance through the system
    if wavelength.get() and power.get() and div.get() and dist.get() and foc.get() and z.get():
        beam = GaussianBeam.GaussianBeam(float(wavelength.get())*1e-9, float(power.get())*1e-3, float(div.get()))
        distances = list(map(float, dist.get().split(',')))
        focal_lengths = list(map(float, foc.get().split(',')))
        if xw.get() and not yw.get():
            beam.lensSystemIntensity(distances, focal_lengths, float(z.get()), xw=float(xw.get())/100)
        elif not xw.get() and yw.get():
            beam.lensSystemIntensity(distances, focal_lengths, float(z.get()), yw=float(yw.get())/100)
        elif xw.get() and yw.get():
            beam.lensSystemIntensity(distances, focal_lengths, float(z.get()), xw=float(xw.get())/100, yw=float(yw.get())/100)
        else:
            beam.lensSystemIntensity(distances, focal_lengths, float(z.get()))

# Labels are created to indicate what the entries are for
tk.Label(master, text='Wavelength (nm)').grid(row=0, column=0)
tk.Label(master, text='Power (mW)').grid(row=1, column=0)
tk.Label(master, text='Beam Divergence (degrees)').grid(row=2, column=0)
tk.Label(master, text='Lens Distances (m)').grid(row=3, column=0)
tk.Label(master, text='Lens Focal Points (m)').grid(row=4, column=0)
tk.Label(master, text='Measurement Distance (m)').grid(row=5, column=0)
tk.Label(master, text='x-axis width (cm)').grid(row=6, column=0)
tk.Label(master, text='y-axis width (cm)').grid(row=7, column=0)

# Two StringVar objects are made for the parameters to be given to the user
W = tk.StringVar()
theta = tk.StringVar()
power_R = tk.StringVar()

# Entries are created to enter parameters of the laser
wavelength = tk.Entry(master)
power = tk.Entry(master)
div = tk.Entry(master)

# Entries are made to enter parameters of the lens system
dist = tk.Entry(master)
foc = tk.Entry(master)

# Entries are made to enter parameters of measurement area
z = tk.Entry(master)
xw = tk.Entry(master)
yw = tk.Entry(master)

# The entries are alligned on the grid
wavelength.grid(row=0, column=1)
power.grid(row=1, column=1)
div.grid(row=2, column=1)
dist.grid(row=3, column=1)
foc.grid(row=4, column=1)
z.grid(row=5, column=1)
xw.grid(row=6, column=1)
yw.grid(row=7, column=1)

# Labels are made to give the user parameters about the beam exiting the system
tk.Label(textvariable=power_R).grid(row=5, column=3)
tk.Label(textvariable=W).grid(row=6, column=3)
tk.Label(textvariable=theta).grid(row=7, column=3)
power_R.set('Power Recieved: ')
W.set('Beam Diameter: ')
theta.set('Beam Divergence: ')

# Buttons are made so the user can exit, update the parameters, or create graphs
tk.Button(master, text='Quit', command=master.quit).grid(row=8, column=0)
tk.Button(master, text='Plot Width', command=width_plot).grid(row=8, column=1)
tk.Button(master, text='Plot Irradiance', command=intensity_plot).grid(row=8, column=2)
tk.Button(master, text='Update', command=update).grid(row=8, column=3)

# The main loop is then executed
master.mainloop()

