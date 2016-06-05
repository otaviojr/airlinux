#!/usr/bin/python

import sys
import os
import getopt
import platforms as platforms

platform=''
destination=''

try:
    myopts, args = getopt.getopt(sys.argv[1:],"p:a:d:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -p platform [specifc commands]" % sys.argv[0])
    sys.exit(2)

for o,a in myopts:
    if o == '-p':
        platform=a
    elif o == '-d':
        destination=a

if not os.path.isdir(destination):
    print "Destination does not exists or is not a directory"
    sys.exit(2)
else:
    if not os.path.isdir(os.path.join(destination,"dist")):
        os.mkdir(os.path.join(destination,"dist"))
    if not os.path.isdir(os.path.join(destination,"packages")):
        os.mkdir(os.path.join(destination,"packages"))
        
platforms.process_platform(platform,sys.argv[1:])
