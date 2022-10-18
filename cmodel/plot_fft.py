#! /usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------

import sys
import numpy as np
import math
import matplotlib as mptlib
import pylab as plt
from scipy import signal

# Get all value from xil_gen_sig
from xil_gen_sig import *

YSIG_FILENAME = "ysig.txt"
SPECTRESIG_FILENAME = "spectre_out.txt"
FREQS_FILENAME = "freqs.txt"
XFFT_FILENAME = "xfft_out.txt"

out_re = []
out_im = []
out_module = []

with open(XFFT_FILENAME, "r") as fp:
    for line in fp:
        re, im = line.split(",")
        re = float(re)
        im = float(im) 
        out_re.append(re)
        out_im.append(im)
        out_module.append(math.sqrt(math.pow(re,2) + math.pow(im,2)))

print(f"Size of output {len(out_re)}")


fix, ax = plt.subplots(1,2)
ax[0].plot(t, y, label = "wave")
ax[0].legend()
spectrum, freqs, line = ax[1].magnitude_spectrum(y,
                        Fs=N/T,
                        ds="steps-mid",
                        window=mptlib.mlab.window_none,
                        label="fft (magnitude_spectrum)")
ax[1].plot(freqs, out_module[:len(freqs)],
           label = "freqs (module calculée xilinx)")
ax[1].legend()
plt.show()

