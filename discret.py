import numpy as np
import pylab as plt

# Freq
f0 = 1
# Temps total en seconde
T = 1
# Nombre de points:
N = 100
# Fréquence d'échantillonage :
print(f"fs = {N/T} Hertz")
# 40 points de 0 à 39
t = np.linspace(0, T, N)
y = np.sin(2*np.pi*f0*t)



fix, ax = plt.subplots(1,2)
ax[0].stem(t, y, 'b', markerfmt="b.")
ax[1].magnitude_spectrum(y, Fs=N/T, ds="steps-mid")
plt.show()

