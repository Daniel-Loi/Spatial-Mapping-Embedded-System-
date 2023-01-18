import math
import numpy
import open3d
numPts = 32

dataPoints = open3d.io.read_point_cloud("test1.xyz", format = "xyz")
print("PCD Array: \n", numpy.asarray(dataPoints.points))

#Graph visualization
open3d.visualization.draw_geometries([dataPoints])

xyplane = []
totalpts = numPts*10
for i in range(totalpts):
    xyplane.append([i])

lines = []

for j in range(1,11): #Goes to the next slice 
    for i in range(numPts*(j-1),numPts*j-1):
        lines.append([xyplane[i],xyplane[i+1]])
    lines.append([xyplane[i],xyplane[(j-1)*numPts]])
 
            
for i in range(0,numPts*9):
    lines.append([xyplane[i], xyplane[i+numPts]])


#3D visualization with lines
line_set= open3d.geometry.LineSet(
    points = open3d.utility.Vector3dVector(numpy.asarray(dataPoints.points)),
    lines = open3d.utility.Vector2iVector(lines),
    )

open3d.visualization.draw_geometries([line_set])
