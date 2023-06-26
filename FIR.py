import numpy as np
from scipy.signal import firwin, lfilter
import matplotlib.pyplot as plt

cutoff_hz = 600.0

sample_rate = 22222

numtaps = 512

fir_coefficients = firwin(numtaps, cutoff_hz/sample_rate)

duration_sec = 4.0
t = np.arange(int(duration_sec * sample_rate)) / sample_rate
input_signal = np.sin(4 * np.pi * cutoff_hz * t)

filtered_signal = lfilter(fir_coefficients, 1.0, input_signal)

plt.figure(figsize=(14, 6))
plt.plot(t, input_signal, label='Orjinal Sinyal')
plt.plot(t, filtered_signal, alpha=0.7, label='Filtre Sinyali')
plt.title('Orjinal ve Filtre Sinyali')
plt.legend()
plt.show()
