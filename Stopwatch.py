import time
from pynput import keyboard
import threading
import os
true = True
laps = ''
seconds = 0
timer_running = true

#actual stopwatch
def timer():
    global seconds
    while true:
        if timer_running:
            minutes, sec = divmod(seconds, 60)
            print(f"Time: {minutes:02}:{sec:02} | You've lapped at:{laps}", end="\r")
            time.sleep(1)
            seconds += 1
            
#stopwatch features
def on_press(key):
    global seconds, laps, timer_running
    minutes, sec = divmod(seconds, 60)
    try:                
        if key.char == 'l':
            if laps != '':
                laps += ','
            if minutes > 0:
                laps += f' {minutes:02}:{sec:02}'
            else:
                laps += f' :{sec:02}'
        
        elif key.char == 'r':
            seconds = 0
            laps = ''
            os.system("cls")
            print("\rTimer has been rebooted")
            
        elif key.char == 's':
            minutes, sec = divmod(seconds, 60)
            timer_running = not timer_running
            if not timer_running:
                print(f"\nTimer is paused at {minutes:02}:{sec:02}")
            if timer_running:
                print("Timer is started")
                
    except AttributeError:
        os.system("cls")
        print("\rSpecial characters not permitted")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
#starting the timer as a thread with daemon so esc becomes the program killer instead of ctrlC
timer_thread = threading.Thread(target=timer, daemon=true)
timer_thread.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
