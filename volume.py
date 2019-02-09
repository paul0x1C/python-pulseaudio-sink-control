#!/usr/bin/env python3
## -*- coding: utf-8 -*-

import subprocess
import argparse

"""
sample commands:
    ./volume.py -v+50%
    ./volume.py -v-10%
    ./volume.py -v20%

    ./volume.py -mtoggle
    ./volume.py -mtrue

sample i3 config:
    bindsym XF86AudioRaiseVolume exec --no-startup-id ~/.config/i3/volume.py -v+5%
    bindsym XF86AudioLowerVolume exec --no-startup-id ~/.config/i3/volume.py -v-5%

    bindsym Shift+XF86AudioRaiseVolume exec --no-startup-id ~/.config/i3/volume.py -v+1%
    bindsym Shift+XF86AudioLowerVolume exec --no-startup-id ~/.config/i3/volume.py -v-1%

    bindsym XF86AudioMute exec --no-startup-id ~/.config/i3/volume.py -mtoggle
"""

parser = argparse.ArgumentParser()
parser.add_argument("-v", help="absolute volume like '50%', relative change like '-10%' or 'mute-toggle'")
parser.add_argument("-m", help="mute: toggle, true or false")

def get_cmd_output(command):
    result = subprocess.check_output(command, shell=True) # run command, store result
    return result.decode()

args = parser.parse_args()
if args.m in ["toggle", "true", "false"]:
    pa_command = "set-sink-mute"
    pa_argument = args.m
elif args.v:
    pa_command = "set-sink-volume"
    pa_argument = args.v
else:
    pa_command = None
    raise SyntaxError("invalid command")

default_sink = get_cmd_output("pactl info | grep 'Default Sink'")[14:].strip('\n') # grep the default sink

if pa_command:
    get_cmd_output("pactl {} {} {}".format(pa_command, default_sink, pa_argument)) # run the final pactl command
