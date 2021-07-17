import matplotlib.pyplot as plt
import numpy as np

traces = np.load('./DATA/LINE_EW_PERIHAKA_100.npy')

rms = np.percentile(traces, 99)
scale =1
sr = 4

fig, ax = plt.subplots()
ax.imshow(traces, aspect='auto', interpolation='bilinear', vmin=-rms*scale, vmax = rms*scale, cmap='bwr', extent=[1000, 3000, traces.shape[0]*sr, 0])
plt.show()