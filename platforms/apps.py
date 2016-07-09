#!/usr/bin/python

import sys
import os
import getopt
import subprocess

sys.path.append(os.path.join("util"))
import yml_util as yml_util

arch=''
system=''
destination=''
cross_tools=''

print sys.argv

try:
    myopts, args = getopt.getopt(sys.argv[1:],"p:a:d:s:c:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -a arch [specifc commands]" % sys.argv[0])
    sys.exit(2)

for o,a in myopts:
    if o == '-a':
        arch=a
    elif o == '-s':
        system=a
    elif o == '-d':
        destination=a
    elif o == '-c':
        cross_tools=a

print "Building tools for %s" % arch

config = yml_util.load_config(os.path.join(sys.path[0],"apps_"+system+".yml"))
if config == None:
    print("Config file not found for: " + arch)
else:
    packages = []
    packages_names = []
    for package in config["packages"]:
        package_name = package["package"]
        dependencies = yml_util.load_config(os.path.join(os.path.dirname(".."),"packages",package_name))
        if not dependencies is None:
            for dependencie in dependencies["dependencies"]:
                if not dependencie in packages_names:
                    for p in config["packages"]:
                        if dependencie == p["package"]:
                            packages += p
                            break
                    print("ERROR: Dependencie %s not found in packages." % dependencie)

        print(package)
        packages += [package]
        packages_names += [package["package"]]

    print "Configuring packages: %s" % packages_names
    for package in packages:
        app = [os.path.join("packages",package["package"],package["script"])]
        os.chmod("".join(app),0775)
        if "parameters" in package and package["parameters"] != None:
            app += package["parameters"]
        app += [destination,arch,cross_tools]
        print "Executing: %s" % app
        subprocess.call(app)
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
