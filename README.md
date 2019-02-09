# python-pulseaudio-sink-control
simple script to change volume and mute-status for the current default pulse audio sink

command examples:

    ./volume.py -v+50%
    ./volume.py -v-10%
    ./volume.py -v20%

    ./volume.py -mtoggle
    ./volume.py -mtrue

i3 config example:

    bindsym XF86AudioRaiseVolume exec --no-startup-id ~/.config/i3/volume.py -v+5%
    bindsym XF86AudioLowerVolume exec --no-startup-id ~/.config/i3/volume.py -v-5%

    bindsym Shift+XF86AudioRaiseVolume exec --no-startup-id ~/.config/i3/volume.py -v+1%
    bindsym Shift+XF86AudioLowerVolume exec --no-startup-id ~/.config/i3/volume.py -v-1%

    bindsym XF86AudioMute exec --no-startup-id ~/.config/i3/volume.py -mtoggle
