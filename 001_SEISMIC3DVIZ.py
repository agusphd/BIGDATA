# https://docs.pyvista.org/plotting/widgets.html
import pyvista as pv
import numpy as np


#volume preparation
values = np.load('./DATA/volve.npy')
vol = pv.UniformGrid()
vol.dimensions = values.shape
vol.origin = (0, 0, 0)  # The bottom left corner of the data set
vol.spacing = (1, 1, 1)  # These are the cell sizes along each axis
vol.point_arrays["Amplitudes"] = values.flatten(order="F")  # Flatten the array!


# cube
# vol.plot(show_edges=False,cmap='RdGy', clim=[-5, 5], opacity=1)


# # slice
# slices = vol.slice_orthogonal(x=50, y=50, z=50)
# slices.plot(cmap='RdGy', clim=[-5, 5])

# interactive slice
p = pv.Plotter(notebook=False)
p.add_mesh_slice_orthogonal(vol,show_edges=False,cmap='RdGy', clim=[-5, 5], opacity=1)
p.show()



## path
# def path(y):
#     a = 110.0 / 160.0 ** 2
#     x = a * y ** 2 + 0.0
#     return x, y
#
# x, y = path(np.arange(vol.bounds[2], vol.bounds[3], 15.0))
# zo = np.linspace(9.0, 11.0, num=len(y))
# points = np.c_[x, y, zo]
# spline = pv.Spline(points, 15)
# slc = vol.slice_along_line(spline)
# p = pv.Plotter()
# p.add_mesh(slc, cmap='RdGy', clim=[-5, 5])
# p.add_mesh(vol.outline())
# p.show(cpos=[1, -1, 1])


## boxstair
# bounds = [100,200, 100,200, 100,200]
# clipped = vol.clip_box(bounds)
# p = pv.Plotter()
# p.add_mesh(clipped, cmap='RdGy', clim=[-5, 5])
# p.show()