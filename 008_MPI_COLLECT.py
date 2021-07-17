import numpy as np
import matplotlib.pyplot as plt


chunk1 = np.load('./DATA/chunk1.npy')
chunk2 = np.load('./DATA/chunk2.npy')
chunk3 = np.load('./DATA/chunk3.npy')
chunk4 = np.load('./DATA/chunk4.npy')


traces = np.load('./DATA/LINE_EW_PERIHAKA_100.npy')

rms = np.percentile(traces, 99)
scale =1
fig, ax = plt.subplots()
ax.imshow(traces, aspect='auto', interpolation='bilinear', vmin=-rms*scale, vmax = rms*scale, cmap='bwr')

traces = np.hstack((chunk1, chunk2, chunk3, chunk4))
rms = np.percentile(traces, 99)
fig, ax = plt.subplots()
ax.imshow(traces, aspect='auto', interpolation='bilinear', vmin=-rms*scale, vmax = rms*scale, cmap='bwr')

plt.show()