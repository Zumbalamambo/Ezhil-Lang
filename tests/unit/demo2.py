#!/usr/bin/python
# -*- coding: utf-8 -*-

import ezhiltests, os

from ezhil import EzhilFileExecuter

program = u"""# மாதிரி =>  முடிவிலா சுழற்சி
# கூகிள் மொழிபெயர்ப்பு பயன்படுத்தி

i = 0
@( i < 100 ) வரை
 i = i + 1
பதிப்பி "வணக்கம் >> ", i
முடி
"""

print program
obj = EzhilFileExecuter( file_input = [program], debug=False, redirectop = not False, TIMEOUT = 10 ) # 2 minutes

# actually run the process
obj.run()

# get executed output in 'progout' and name of the two tmp files to cleanup
[tmpfile,filename,progout] = obj.get_output()

#os.unlink( tmpfile )
#os.unlink( filename )

if obj.exitcode != 0 and EzhilWeb.error_qualifiers(progout):
    failed = True
else:
    failed = False
    
print u"output = "
print u"%s,%s"%(progout.decode('utf-8'), str(failed))

