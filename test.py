#!/usr/bin/env python2
# Program for testing libMSRx05
#
# Copyright Kirils Solovjovs, 2013
import libMSRx05 as msr
import sys
device = msr.x05('/dev/ttyUSB0',True)

device.setLED(7)

print "Firmware Version: " + device.getFirmwareVersion()
print "Device Model: " + device.getDeviceModel()
print "Coercivity: " + ("High" if device.getCo() else "Low")

#print "Full self test (please swipe a card until green light blinks):",
#sys.stdout.flush()
#if device.test():
#  print 'OK'
#else:
#  print 'FAILED'

device.reset()

#print device.setBPC([7,5,5]);
#print device.setBPI([1,0,1]);
#print device.writeISO(['%34XX%23_4?',None,';01234567890:;<=>0123?'])
#print device.eraseTrack([1,1,1]);

print "Please swipe the original to clone..."
a = device.readRaw()

print "Please swipe the card to be written...",
sys.stdout.flush()

#this erases the tracks which are empty on the original
if (device.eraseTrack(map(lambda x: len(x)==0,a))):
  print "again..."
  sys.stdout.flush()
if device.writeRaw(a): print 'ok'
else: print 'failed'

print "Please swipe the newly written card again to verify contents..."
print device.readISO()


device.close()
