#!/usr/bin/python3
""" Fabric script that generates a .tgz
archive from the contents of the web_staticfolder
of your AirBnB Clone repo, using the the function do_pack
"""
from fabric.api import *

def do_pack():
    local('sudo mkdir -p versions')
