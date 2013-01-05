#!/usr/bin/env python2

import libMSRx05 as msr
import sys
reader = msr.x05('/dev/ttyUSB0')

#print "Full self test (please swipe a card until green light blinks):",
#sys.stdout.flush()
#if reader.test():
#  print 'OK'
#else:
#  print 'FAILED'

print "Firmware Version: " + reader.getFirmwareVersion()
print "Device Model: " + reader.getDeviceModel()

#print reader.setBPC([7,5,5]);
#print reader.setBPI([1,0,1]);
#print reader.writeISO(['%34XX%23_4?',';123123?',';01234567890:;<=>0123?'])
#print reader.writeISO(['',';123123?',''])
#print reader.eraseTrack([1,1,1]);

#print "Write something"



print reader.readISO()
#print "RAWW Read, Baby!"
#a = reader.readRaw();
#print a
#print [len(a[0]), len(a[1]), len(a[2])]
#print reader.readISO()
#print "Erasing..."
#reader.eraseCard(True, True, True)
#print "Reading..."
#print reader.readIso()

# woo card copying works!
#reader.writeISO(reader.readISO())

#print reader.readIso()
reader.close()
