import os
import sys
import subprocess

def process_platform(platform,argv):
    if os.path.isfile("./platforms/"+platform+".py"):
        print("Executing platform: " + platform)
        subprocess.call(["./platforms/"+platform+".py"] + sys.argv[1:])
    else:
        print("Unknown platform (%s)." % platform)
        print("TODO: List available platforms")
        sys.exit(2)
