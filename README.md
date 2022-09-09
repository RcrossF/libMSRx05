libMSRx05
======
Forked from 0ki to add python3 support and fix some bugs I was running into. It's still far from perfect but was all I needed for my project.

Pyhton library for interfacing MSRx05 and MSRx06 Magnetic Stripe Card Readers/Writers

This fully implements the communication protocol.


Please let me know about any bugs.

=====
Missing:
It would be great if someone implemented a layer of RAW write and RAW read functions that work with human-readable contents
Functions placeholders are already in place at the bottom of the lib file

  print device.writeRawText(['123','123','123'],[1,1,1],[5,5,5],[0,0,0])

Some code may be found here: https://github.com/lid/MagTool/blob/master/AppController.m




=====
Info on MagStripe: http://www.gae.ucm.es/~padilla/extrawork/stripe.html
