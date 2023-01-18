

#Modify the following line with your own serial port details
#   Currently set COM3 as serial port at 115.2kbps 8N1
#   Refer to PySerial API for other options.  One option to consider is
#   the "timeout" - allowing the program to proceed if after a defined
#   timeout period.  The default = 0, which means wait forever.

import serial
import math
import numpy
import open3d

s = serial.Serial('COM4', 115200)
k = 0
x = []
y = []
z = []
numPts = 32
pi = math.pi

print("Opening: " + s.name)

# reset the buffers of the UART port to delete the remaining data in the buffers
s.reset_output_buffer()
s.reset_input_buffer()

# wait for user's signal to start the program
input("Press Enter to start communication...")
# send the character 's' to MCU via UART
# This will signal MCU to start the transmission
s.write('s'.encode())

# recieve 10 measurements from UART of MCU
for i in range(10):
    
    for j in range(numPts):
        q = s.readline()
        tempstr = q.decode()
        distance = tempstr.split(", ")
        z.insert(k,100*i)
        x.insert(k,(float(distance[1])*math.cos(-j*(2*pi/numPts))))
        y.insert(k,(float(distance[1])*math.sin(-j*(2*pi/numPts))))
        print("Distance measured: " + distance[1] + " x: " ,float(distance[1])*math.cos(j*pi/32), "y: ",float(distance[1])*math.sin(j*pi/32), k)
        k = k +1
    
           
# the encode() and decode() function are needed to convert string to bytes
# because pyserial library functions work with type "bytes"


#close the port
print("Closing: " + s.name)
s.close()

##########################################################
#New file for open3d visualization
if __name__ == "__main__":
    file = open("test1.xyz","w")
    k = 0

    for i in range(10):
        for j in range(numPts):
            file.write('{0:f} {1:f} {2:f}\n'.format(x[k],y[k],z[k]))
            k = k + 1
        
    file.close()

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










