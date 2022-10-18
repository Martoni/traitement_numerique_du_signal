#! /usr/bin/python3
# -*- coding: utf-8 -*-
""" fourrier_fixed_size
"""
import sys
import numpy as np
import BigNumber
import pylab as plt
from fxpmath import Fxp
from scipy import signal

# Temps total en seconde
T = 10
# Nombre de points:
N = 2**7
#N = 100
# Fréquence d'échantillonage :
Fs = N/T
print(f"fs = {Fs} Hertz")

# Frequence du signal
Sf0 = 2

f0 = (Sf0 * Fs)/T

# Décalage en seconde:
retard = 5

#temps: 0 points de 0 à N-1
t = np.linspace(0, T, N)
# morlet wavelet
y = np.cos(2*np.pi*f0*t)*np.exp(-np.power(t-retard,2)/2)

YTYPE="S1.15"
ysint = Fxp(y, dtype=YTYPE)

# plot du spectre «python»
fix, ax = plt.subplots(1,2)
#ax[0].plot(t, y, label = "y(float)")
ax[0].plot(t, ysint, label = f"y({YTYPE})")
ax[0].legend()
magnitude, freqs, _ = ax[1].magnitude_spectrum(y, Fs=N/T, ds="steps-mid", label=f"fft (Fs={Fs} Hz)")

DTYPE="S8.8"
D2TYPE="S16.16"

fixpi = Fxp(np.pi, dtype="U3.13")

# transformée de fourrier
freqs_real = np.array([])
freqs_img = np.array([])
for k in range(len(freqs)):
    listreal = []
    listimg = []
    for n in range(N):
        angle = Fxp(2*fixpi*Fxp(k*n, dtype="U16.0")/N, dtype=D2TYPE)
        listreal.append(Fxp(y[n], dtype=YTYPE)*Fxp( np.cos(angle), dtype=YTYPE))
        listimg.append (Fxp(y[n], dtype=YTYPE)*Fxp(-np.sin(angle), dtype=YTYPE))
    xkreal = Fxp(np.array(listreal).sum(), dtype=DTYPE)
    xkimg  = Fxp(np.array(listimg ).sum(), dtype=DTYPE)
    print(f"Freq {k}/{Fs} ({k*T/N}) -> {np.sqrt(xkreal*xkreal + xkimg*xkimg)})")
    freqs_real = np.append(freqs_real, xkreal)
    freqs_img = np.append(freqs_img, xkimg)

fourrier_power = Fxp(Fxp(freqs_img*freqs_img, dtype=DTYPE) + Fxp(freqs_real*freqs_real, dtype=DTYPE), dtype=DTYPE)
fourrier_module = Fxp((2/N)*Fxp(np.sqrt(fourrier_power), dtype=DTYPE), dtype=DTYPE)
fourrier_power[0].info()

# plot du spectre calculé
ax[1].plot(freqs, fourrier_module[:len(freqs)], label = "freqs (calculée)")
#ax[1].plot(k, fourrier_power, label = "freqs (puissance calculée)")
ax[1].legend()
plt.show()

