#!/usr/bin/python3

import os.path
file = "./dump"
# 1 KB of garbage ... 
garbage = """
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111111111111111111
"""

if os.path.exists(file):
	os.remove(file)

dump = open(file,"w")
#Enter needed file size in range 
#write 1024(=1MB)*1024(=1GB)*10(=10GB) of garbage into dump file
for i in range(1024*1024*60):
        dump.write(garbage)
        #print only each MB progress
        if (i % 1024) == 0: 
                print (str(i/1024))
dump.close()

"""		
while ((os.path.getsize(file)/(1024*1024*1024)) < 1):
	dump = open(file,"a")
	dump.write(garbage)
	dump.close()
	print (os.path.getsize(file)/(1024*1024*1024))
"""
