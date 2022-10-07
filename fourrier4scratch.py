#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" fourrier4scratch
"""
import numpy as np
import pylab as plt
from scipy import signal

# Freq
f0 = 2 
# Temps total en seconde
T = 10
# Nombre de points:
N = 100
# Fréquence d'échantillonage :
print(f"fs = {N/T} Hertz")
# Décalage en seconde:
retard = 5

#temps: 0 points de 0 à N-1
t = np.linspace(0, T, N)
# morlet wavelet
y = np.cos(2*np.pi*f0*t)*np.exp(-np.power(t-retard,2)/2)

# transformée de fourrier
freqs_real = np.array([])
freqs_img = np.array([])
for k in range(N):
    listreal = []
    listimg = []
    for n in range(N):
        angle = 2*np.pi*k*n/N
        listreal.append(y[n]*(np.cos(angle)))
        listimg.append(y[n]*(-np.sin(angle)))
    xkreal = np.array(listreal).sum()
    xkimg = np.array(listimg).sum()
    freqs_real = np.append(freqs_real, xkreal)
    freqs_img = np.append(freqs_img, xkimg)

fourrier_module = (2/N)*np.sqrt(np.power(freqs_img, 2) + np.power(freqs_real, 2))

#fréquence: 0 points de 0 à N-1
k = np.linspace(0, T, N)

fix, ax = plt.subplots(1,2)
ax[0].plot(t, y, label = "wave")
ax[0].legend()
ax[1].magnitude_spectrum(y, Fs=N/T, ds="steps-mid", label="fft (python)")
#ax[1].plot(k, fourrier_module, label = "freqs (calculée)")
ax[1].plot(k, fourrier_module, label = "freqs (module calculée)")
ax[1].legend()
plt.show()

