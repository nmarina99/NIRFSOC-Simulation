'''
A GUI for creating fast intensity plots for Gaussian beams
Utilizes the tkinter, numpy, and matplotlib packages, and imports the GaussianBeam.py file
Created On: 10/23/19
Created By: Nicholas Marina
Last Updated: 10/25/19
'''

import tkinter as tk
import numpy as np
import GaussianBeam

def plot():
    # Plots the intensity map of the Gaussian beam with the parameters specified in the GUI
    print(xw.get())
    beam = GaussianBeam.GaussianBeam(float(wl.get())*1e-9, float(P.get())*1e-3, float(theta.get()))
    if not xw.get() and not yw.get == '':
        beam.intensityPlot(float(d.get()))
    elif not xw.get() and yw.get:
        beam.intensityPlot(float(d.get()), yw=float(yw.get())/1000)
    elif xw.get() and not yw.get():
        beam.intensityPlot(float(d.get()), xw=float(xw.get())/100)
    else:
        beam.intensityPlot(float(d.get()), xw=float(xw.get())/100, yw=float(yw.get())/100)

def update_params():
    # Updates parameters calculated on the GUI's text labels
    beam = GaussianBeam.GaussianBeam(float(wl.get())*1e-9, float(P.get())*1e-3, float(theta.get()))
    W = beam.waist*np.sqrt(1 + (float(d.get())/beam.z0)**2) 
    I = beam.I*((beam.waist/W)**2)
    BWs.set("Beam Waist: " + np.format_float_scientific(1000000*beam.waist, 3) + " um")
    BW.set("Beam Width: " + np.format_float_scientific(100*W, 3) + " cm")
    MI.set("Maximum Intensity: " + np.format_float_scientific(I, 3) + " W/m²")

# The window is initialized
master = tk.Tk()
master.title('Gaussian Beam Intensity')
master.geometry('500x150')

# Labels are made to specify what parameters each textbox cooresponds to
tk.Label(master, text="Wavelength (nm)").grid(row=0)
tk.Label(master, text="Power (mW)").grid(row=1)
tk.Label(master, text="Divergence (degrees)").grid(row=2)
tk.Label(master, text="Distance (m)").grid(row=3)
tk.Label(master, text="x-axis Length (cm)").grid(row=4)
tk.Label(master, text="y-axis Length (cm)").grid(row=5)

# StringVar objects are used for the Beam Waist, Beam Width, and Maximum Intensity labels, so they can be adjusted to input parameters
BWs = tk.StringVar()
BW = tk.StringVar()
MI = tk.StringVar()
tk.Label(master, textvariable=BWs).grid(row=3, column=2)
tk.Label(master, textvariable=BW).grid(row=4, column=2)
tk.Label(master, textvariable=MI).grid(row=5, column=2)
# The StringVar objects are intialized to be blank
BWs.set("Beam Waist:")
BW.set("Beam Width:")
MI.set("Maximum Intensity:")

# Entry boxes are created for the beam parameters
wl = tk.Entry(master)
P = tk.Entry(master)
theta = tk.Entry(master)
d = tk.Entry(master)
xw = tk.Entry(master)
yw = tk.Entry(master)

# Entry boxes are then placed on the grid next to the cooresponding labels
wl.grid(row=0, column=1)
P.grid(row=1, column=1)
theta.grid(row=2, column=1)
d.grid(row=3, column=1)
xw.grid(row=4, column=1)
yw.grid(row=5, column=1)

# Buttons are created so the user can quit, plot the intensity, and update the output text
tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0)
tk.Button(master, text='Plot', command=plot).grid(row=6, column=1)
tk.Button(master, text='Update', command=update_params).grid(row=6, column=3)

# The main loop of the window is executed
master.mainloop()

