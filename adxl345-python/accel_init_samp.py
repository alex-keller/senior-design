#!/usr/bin/env python
# accelerometer initialize and sample script
# Alex Keller 2/2/2016

from adxl345 import ADXL345
import numpy as np

# constants - offset register addresses
OFSX = 0x1E
OFSY = 0x1F
OFSZ = 0x20
# ALPHA - FOR FILTERING
ALPHA = 0.1896

adxl345 = ADXL345()
# set range to +/- 4g
adxl345.setRange(0x00)
axes = adxl345.getAxes(True)
print "ADXL345 on address 0x%x:" % (adxl345.address)
print "   x = %.3fG" % ( axes['x'] )
print "   y = %.3fG" % ( axes['y'] )
print "   z = %.3fG" % ( axes['z'] )
raw_input("Press any key to continue")

# find offset values
''' use average of samples
_xTot = 0
_yTot = 0
_zTot = 0
count = 1000
for i in range(count):
    axes = adxl345.getAxes(True);
    _xTot = _xTot + axes['x'];
    _yTot = _yTot + axes['y'];
    _zTot = _zTot + axes['z'];
_xoffset = int(-round(_xTot/count*256/3.9));
_yoffset = int(-round(_yTot/count*256/3.9));
_zoffset = int(-round(_zTot/count*256/3.9));
'''
# use median of samples - need NumPy
_xTot = []
_yTot = []
_zTot = []
count = 1000
for i in range(count):
    axes = adxl345.getAxes(True);
    _xTot.append(axes['x'])
    _yTot.append(axes['y'])
    _zTot.append(axes['z'])
_xoffset = int(-round(np.median(_xTot)*256/3.9));
_yoffset = int(-round(np.median(_yTot)*256/3.9));
_zoffset = int(-round(np.median(_zTot)*256/3.9));

#x_min = axes['x']
#x_max = axes['x']
#y_min = axes['y']
#y_max = axes['y']
#z_min = axes['z']
#z_max = axes['z']
# for debug
print _xoffset
print _yoffset
print _zoffset
adxl345.writeReg(OFSX,_xoffset)
adxl345.writeReg(OFSY,_yoffset)
adxl345.writeReg(OFSZ,_zoffset)
XX = adxl345.readReg(OFSX)
YY = adxl345.readReg(OFSY)
ZZ = adxl345.readReg(OFSZ)
print "XX =", XX
print "YY =", YY
print "ZZ =", ZZ

# sample
#for i in range(10000):
#        axes = adxl345.getAxes(True)
#        print "ADXL345 on address 0x%x:" % (adxl345.address)
#        print "   x = %.3fG" % ( axes['x']-_xoffset )
#        print "   y = %.3fG" % ( axes['y']-_yoffset )
#        print "   z = %.3fG" % ( axes['z']-_zoffset )
	#time.sleep(1)
#	raw_input("Press any key to continue")

for i in range(10000):
        axes = adxl345.getAxes(True)
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )
        raw_input("Press any key to continue")            
   
       # raw_input("press any key to continue")
#	if axes['x'] >  x_max:
#		x_max = axes['x']
#	if axes['x'] < x_min:
#		x_min = axes['x']
#	if axes['y'] > y_max:
#		y_max = axes['y']
#	if axes['y'] < y_min:
#		y_min = axes['y']
#	if axes['z'] > z_max:
#		z_max = axes['z']
#	if axes['z'] < z_min:
#		z_min = axes['z']
#	print "X Max: ", x_max, " X Min: ", x_min
#	print "Y Max: ", y_max, " Y Min: ", y_min
#	print "Z Max: ", z_max, " Z Min: ", z_min	 
#	raw_input("press any key")
