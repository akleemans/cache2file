#!/usr/bin/python
# -*- coding: ascii -*-

######################################
# by akleemans, 12/12/12
# Extracts a file (for example mp3)
# from a chrome about:cache HTML-file.
######################################

import time
import sys

if len(sys.argv) != 2: print "[+] Please provide filename as argument."
else: filename = sys.argv[1]

print "[+] Converting", filename
t1 = time.time()

source = open(filename, 'rb')
target = open(filename + ".mp3", 'wb')
content = source.read().split("</pre><hr><pre>")[2].split("\n")
source.close()

for line in content:
    l = line[:74].strip().split("  ")
    del l[0]
    for i in l:
        target.write(chr(int(i, 16)))
target.close()

print "[+] Wrote file in", round(time.time()-t1, 2), "s"
