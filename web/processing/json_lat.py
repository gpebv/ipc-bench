import sys, os
import json
import matplotlib
matplotlib.use("Agg")
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pylab as pyl
import re

class Hardware:
	def __init__(self, data, dat):
		self.name=data[1]
		self.cores=data[0]
		self.numa=data[2]
		self.mem=data[3]
		self.os=data[4]
		self.virtualized=data[5]
		self.dat=dat
	def jsonize(self):
		return self.__dict__

class Lat_data:
     def __init__(self, x, y, v):
         self.x = x
         self.y = y
	 self.v = v
     def jsonize(self):
	return self.__dict__

def ComplexHandler(Obj):
        return Obj.jsonize()

def get_data(filename):
  data = np.loadtxt(filename)

  x_tmp = []
  y_tmp = []
  v_tmp = []
  retdata = []
  for i in range(0, len(data)):
    for j in range(0, len(data[i])):
      x_tmp.append(i)
      y_tmp.append(j)
      v_tmp.append(data[i][j])

  for i in range(0, len(x_tmp)):
	retdata.append(Lat_data(x_tmp[i], y_tmp[i], v_tmp[i] ))

  return retdata


# ---------------------------
# Handle command line args

if len(sys.argv) < 2:
  print "usage: python plot_lat.py <input file> <title> <output_dir> <num_cores> <[hardware]> [fix-scale]"
  sys.exit(0)

input_file = sys.argv[1]

fix_scale = 0
if len(sys.argv) > 6:
  fix_scale = int(sys.argv[6])



num_cores = int(sys.argv[4])

output_dir = sys.argv[3]

raw_data = np.loadtxt(input_file)
data = get_data(input_file)

hard=Hardware(sys.argv[5].split(','), data)

f=open(output_dir + "/lat_" + sys.argv[2].replace( ".csv",".json"), 'w+')

f.write ( json.dumps(hard, default=ComplexHandler) )

f.close()





