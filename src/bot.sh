#!/bin/bash
#echo start
#/usr/bin/screen -d -m -A -S bot /usr/bin/python3 /opt/bot.py
#/usr/bin/python3 /opt/bot.py >> /dev/shm/pybot.log
tmux new-session -n wine -s css  /opt/bot.py

#bash
#ps ax
#while (true); do sleep 1; done
#echo by
