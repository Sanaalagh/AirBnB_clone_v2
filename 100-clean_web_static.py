# 100-clean_web_static.py
from fabric.api import *
from os import path

env.hosts = ['18.204.10.166', '54.208.220.160']
env.user = "username"

def do_clean(number=0):
    number = int(number) + 1
    local('ls -tr versions/*.tgz | head -n -{} | xargs rm -rf'.format(number))
    
    with cd('/data/web_static/releases'):
        run('ls -tr | head -n -{} | xargs rm -rf'.format(number))

