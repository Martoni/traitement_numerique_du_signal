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


# 0 points de 0 à N-1
t = np.linspace(0, T, N)

# morlet wavelet
y = np.cos(2*np.pi*f0*t)*np.exp(-np.power(t-retard,2)/2)

himg = signal.hilbert(y).imag
hreal = signal.hilbert(y).real

habs = np.sqrt(np.power(himg, 2) + np.power(hreal, 2))

print(f"Valeur moyenne : {np.mean(y)}")

fix, ax = plt.subplots(1,2)
#ax[0].stem(t, y, 'b', markerfmt="b.")
#ax[0].plot(t, y, label = "wave")
ax[0].plot(t, himg, label = "himg")
ax[0].plot(t, hreal, label = "hreal")
ax[0].plot(t, habs, label = "habs")
ax[0].legend()
ax[1].magnitude_spectrum(y, Fs=N/T, ds="steps-mid", label="fft")
ax[1].legend()
plt.show()

