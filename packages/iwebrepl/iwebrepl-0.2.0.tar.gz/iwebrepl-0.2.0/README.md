[![Build Status](https://travis-ci.org/kost/iwebrepl-python.png)](https://travis-ci.org/kost/iwebrepl-python)

iwebrepl
======
Python module to handle micropython websocket (WS) repl protocol interactively. It is modified original implementation to make it more user friendly.

Requirements
============

It should work with python3 with simple pip commands:
```
pip install iwebrepl
```

iwebrepl
========

Few webreplcmd examples:
```

iwebrepl --host 192.168.4.1 --password ulx3s
```

Note that you can also specify basic parameters using environment variables:
```
export IWEBREPL_HOST=127.0.0.1
export IWEBREPL_PASSWORD=ulx3s
export IWEBREPL_PORT=8266
```

and then you can just specify command:
```
iwebrepl
```

All options are listed using --help:

```
iwebrepl --help
```


Manual
======

```
usage: iwebrepl [-h] [--host HOST] [--time TIME] [--port PORT] [--verbose]
                [--debug] [--redirect] [--password PASSWORD] [--cmd CMD]
                [--after AFTER] [--before BEFORE]

iwebrepl - connect to websocket webrepl

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -i HOST  Host to connect to
  --time TIME, -t TIME  Delay time to receive response
  --port PORT, -P PORT  Port to connect to
  --verbose, -v         Verbose information
  --debug, -d           Enable debugging messages
  --redirect, -r        Redirect
  --password PASSWORD, -p PASSWORD
                        Use following password to connect
  --cmd CMD, -c CMD     command to execute
  --after AFTER, -A AFTER
                        command to execute after interactive mode
  --before BEFORE, -B BEFORE
                        command to execute before interactive mode

iwebrepl --host 192.168.4.1 --password ulx3s
iwebrepl --host 192.168.4.1 --password ulx3s --cmd 'import os; os.listdir()'

Keyboard:
Keyboard: Ctrl-x to exit, Ctrl-d softreboot, Ctrl-k display help
```

Keyboard shortcuts
======

You can use following keyboard shortcuts:

```
Custom keybindings:
- CTRL-x : to exit WebREPL Terminal
- CTRL-e : Enters paste mode
- CTRL-d: In normal mode does a soft reset (and exit), in paste mode : executes pasted script
- CTRL-c : Keyboard interrupt in normal mode, in paste mode : cancel
- CTRL-r: Backsapce x 20 (to erase current line in chunks) or flush line buffer
- CTRL-u: import shortcut command (writes import)
- CTRL-f: to list files in cwd (ls shorcut command)
- CTRL-n: shows mem info
- CTRL-y: gc.collect() shortcut command
- CTRL-space: repeats last command
- CTRL-t: runs test_code.py if present
- CTRL-w: flush test_code from sys modules, so it can be run again
- CTRL-a: force synchronized mode (better if using wrepl through ssh session)
- CTRL-p: toggle autosuggest mode (Fish shell like) (if not in synchronized mode)
- CTRL-k: prints the custom keybindings (this list)
```

Complete Requirements
============

It should work with python3 with simple pip commands:
```
sudo apt-get update
sudo apt-get install -y python3 python3-pip
sudo pip3 install iwebrepl
```
