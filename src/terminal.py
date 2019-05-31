#!/usr/bin/python

import os

from Alfred import Tools

OS_TERMINAL = 'open -b com.apple.terminal'
term = Tools.getEnv('terminal_path')
terminal = term if term else OS_TERMINAL
path = Tools.getEnv('item1')

cmd = "%s %s" % (terminal, path)
os.popen2(cmd)
