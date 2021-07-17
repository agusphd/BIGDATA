import numpy as np                         # For array based computations and world domination
import matplotlib.pyplot as plt
import segyio

filename = './DATA/shot.sgy'
with segyio.open(filename, 'r', ignore_geometry=True) as segyfile:
    ntraces = segyfile.tracecount
    sr = segyio.tools.dt(segyfile)
    nsamples = segyfile.samples.size
    twt = segyfile.samples
    data = segyfile.trace.raw[:]
    size_mb= data.nbytes/1024**2
    header = segyio.tools.wrap(segyfile.text[0])
# print(header)

clip_percentile = 99
vm = np.percentile(data, clip_percentile)
f'The {clip_percentile}th percentile is {vm:.0f}; the max amplitude is {data.max():.0f}'

fig = plt.figure(figsize=(8, 18))
ax = fig.add_subplot(1, 1, 1)
extent = [1, ntraces, twt[-1], twt[0]]  # define extent
data = data.T

print(data)
np.save('./DATA/seismic.npy', data)
ax.imshow(data, interpolation='bilinear', aspect='auto', cmap="bwr", vmin=-vm, vmax=vm, extent=extent)
ax.set_xlabel('CDP number')
ax.set_ylabel('TWT [ms]')
ax.set_title(f'{filename}')
plt.show()