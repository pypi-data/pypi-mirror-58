import logging
import os
import subprocess
import socket
import sys
import time
import signal

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(sys.stdout))

def connect(instances):
    log.info('>> cloud_sql_proxy called')

    def check_running():
        log.info('>> cloud_sql_proxy - check_running called')

        # Attempt to connect to socket. If we can, that means something is listening - jc 12/20/2019
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(('127.0.0.1', 3306))
        s.close()

        log.info('>> cloud_sql_proxy - result: %s', result)

        if result == 0:
            # We made a connection, something is listening - jc 12/20/2019
            return True
        else:
            return False

    i = 1
    pid = None
    while check_running() is False:
        log.info('>> cloud_sql_proxy starting')
        cmd = ['{}/cloud_sql_proxy'.format(os.path.dirname(__file__)),
               '-instances={}=tcp:3306'.format(instances)]
        print(cmd)
        proxy = subprocess.Popen(cmd)
        pid = proxy.pid
        time.sleep(i)
        i = i*2

    log.info('>> cloud_sql_proxy finished connecting')
    return pid

def disconnect(pid):
    log.info('>> cloud_sql_proxy disconnect called')
    if (pid != None):
        log.info('>> cloud_sql_proxy killing pid {}'.format(pid))
        os.kill(pid, signal.SIGKILL)
    else:
        log.info('>> cloud_sql_proxy no pid found to kill')
