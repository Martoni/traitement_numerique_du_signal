import numpy as np
import pylab as plt

# Freq
f0 = 40 
# Temps total
T = 1
# Nombre de points:
N = 40
# Fréquence d'échantillonage :
print(f"fs = {N/T} Hertz")
# 40 points de 0 à 39
t = np.linspace(0, T, N)
y = np.sin(2*np.pi*f0*t)



fix, ax = plt.subplots()
ax.stem(t, y, 'b', markerfmt="b.")
plt.show()

