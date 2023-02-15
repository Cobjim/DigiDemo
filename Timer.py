#Taken from https://stackoverflow.com/questions/63625031/how-to-create-a-timer-that-times-for-how-long-a-certain-key-is-pressed-in-python
# Modified by Ian Coberly

from pynput.keyboard import Key, Listener
import time

keys_pressed={}  # dictionary of keys currently pressed

def on_press(key): # gets re-called a key repeats
     if key not in keys_pressed:  # if not repeat event
         keys_pressed[key] = time.time() # add key and start time
         
def on_release(key):
     print (key, time.time() - keys_pressed[key])  # time pressed
     del keys_pressed[key] # remove key from active list
     if key==Key.esc:
         return False
         
with Listener(on_press=on_press,on_release=on_release) as listener:
     listener.join()
