#!/usr/bin/python


import signal, os
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print frame

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGHUP, handler)
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGQUIT, handler)
signal.signal(signal.SIGTERM, handler)
while 1:
    time.sleep(1);

