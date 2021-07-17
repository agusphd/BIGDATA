import matplotlib.pyplot as plt
import numpy as np

traces = np.load('./DATA/LINE_EW_PERIHAKA_100.npy')
rms = np.percentile(traces, 99)

scale =1
fig, ax = plt.subplots()
ax.imshow(traces, aspect='auto', interpolation='bilinear', vmin=-rms*scale, vmax = rms*scale, cmap='bwr')
plt.show()

