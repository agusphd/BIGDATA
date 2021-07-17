from collections import defaultdict
from heapq import *
import numpy as np
from scipy.spatial import KDTree
import re
from scipy.interpolate import interp1d
import time

tri = np.load('./DATA/triangraytrace.npy')
topo = np.genfromtxt('./DATA/topo.txt')

#vel gradient
centroide=[]
for i in range(tri.shape[0]):
    c = [[tri[i,0], tri[i,2], tri[i,4]], [tri[i,1], tri[i,3], tri[i,5]]]  # of the form [[x1,x2,x3],[y1,y2,y3]]
    centroide.append((sum(c[0]) / len(c[0]), sum(c[1]) / len(c[1])))
centroide=(np.asarray(centroide))
tri=tri.reshape(tri.shape[0],3,2)

ft = interp1d(topo[:,0], topo[:,1], kind='linear', fill_value='extrapolate')  # function of topo
topoc=ft(centroide[:,0])
depthc=topoc-centroide[:,1]
vel0 = 860*depthc+1700
# sources
source = np.load('./DATA/source.npy')

#receiver
receiv = np.load('./DATA/receiv.npy')

node=np.vstack((source,receiv,centroide))



#########  use KDtree for index
#get 50 neigbours for each point  (faster
tree = KDTree(node, leafsize=node.shape[0]+1)
distances, point = tree.query([node], k=50)
point=point[0]
point=np.array((np.vstack((np.repeat(np.arange(0,point.shape[0],1), point.shape[1]),point.flatten()))).T,dtype=int)


#############djikstra
p1=(node[point[:,0]])
p2=(node[point[:,1]])
dist=np.array((((p2[:,0]-p1[:,0])**2) + ((p2[:,1]-p1[:,1])**2))**0.5)

# topo vel gradv
yp1=ft(p1[:,0])
yp2=ft(p2[:,0])
y1=yp1-p1[:,1]
y2=yp2-p2[:,1]

vp1 = 860*y1+1700
vp2 = 860*y2+1700
vel = (vp1+vp2)/2

np.save('./DATA/velinit',vel)
nettwork=np.column_stack((point,dist/vel))
edges=list(map(tuple, nettwork))

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                next = cost + c
                heappush(q, (next, v2, path))

    return float("inf")


################
start = time.time()
for i in range(source.shape[0]):  #50
    jejak = dijkstra(edges, i, source.shape[0]+i)
    jejak = np.array([float(s) for s in re.findall(r'-?\d+\.?\d*', str(jejak))], dtype=int)
    jejak = jejak[1:len(jejak)]
    jejak = node[jejak, :]
    np.save('./RAYP/ray%s'%i,jejak)

end = time.time()

print("Computation time %f secs" % (end - start))