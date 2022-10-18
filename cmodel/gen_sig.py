#! /usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Author:   Fabien Marteau <fabien.marteau@armadeus.com>
# Created:  18/10/2022
#-----------------------------------------------------------------------------
#  Copyright (2021)  Armadeus Systems
#-----------------------------------------------------------------------------
""" gen_sig
"""
import numpy as np
import matplotlib as mptlib
import pylab as plt
from scipy import signal

YSIG_FILENAME = "ysig.txt"
SPECTRESIG_FILENAME =  "spectre_out.txt"

# Freq
f0 = 2 
# Temps total en seconde
T = 10
# Nombre de points:
N = 1024
# Fréquence d'échantillonage :
print(f"fs = {N/T} Hertz")
# Décalage en seconde:
retard = 5

#temps: 0 points de 0 à N-1
t = np.linspace(0, T, N)
# morlet wavelet
y = np.cos(2*np.pi*f0*t)*np.exp(-np.power(t-retard,2)/2)

with open(YSIG_FILENAME, "w") as fp:
    print(f"Écriture du signal dans {YSIG_FILENAME}")
    for value in y:
        fp.write(f"{value}\n");

fix, ax = plt.subplots(1,2)
ax[0].plot(t, y, label = "wave")
ax[0].legend()
spectrum, freqs, line = ax[1].magnitude_spectrum(y,
                        Fs=N/T,
                        ds="steps-mid",
                        window=mptlib.mlab.window_none,
                        label="fft (magnitude_spectrum)")
print(f"Taille du spectre {len(spectrum)}")
print(f"Taille de freqs {len(freqs)}")

# transformée de fourrier «maison»
freqs_real = np.array([])
freqs_img = np.array([])
for k in range(len(freqs)):
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

fourrier_module = (1/N)*np.sqrt(np.power(freqs_img, 2) + np.power(freqs_real, 2))

ax[1].plot(freqs,
           fourrier_module[:len(freqs)],
           label = "freqs (module calculée «maison»)")
ax[1].legend()
plt.show()

