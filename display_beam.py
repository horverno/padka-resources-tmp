#!/usr/bin/env python
from __future__ import print_function
import rospy
import std_msgs.msg as rosmsg
import nav_msgs.msg as navmsg
import sensor_msgs.msg as senmsg
import geometry_msgs.msg as geomsg
import numpy as np
import csv
import time
import pandas as pd 
import matplotlib.pyplot as plt

#for i in range(9):
i = 1
file_name = ("csv/padka%03d.csv" % (i+1))
points = np.asarray(pd.read_csv(file_name, sep=",",header=None))
plt.plot(points[1,:], points[2,:], 'go-.', lw=2, label=file_name[4:]) 
plt.xlabel("X")
plt.ylabel("Y magassag")
plt.legend()
plt.title(file_name[4:])
#plt.savefig(file_name[4:-3] + "png")
#plt.cla()
plt.show()
