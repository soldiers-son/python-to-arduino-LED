from pyfirmata import Arduino
import tkinter as tk

### Monkey patch for python3.11+ ###
import inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

# Specify the port your Arduino is connected to
# On Windows it might be 'COM3', on Linux/Mac something like '/dev/ttyUSB0'
board = Arduino('COM3')

# Board Pin Connection
LED = 2

# Turns the LED on
def on():
    board.digital[LED].write(1)   # Turn LED on

# Turn LED off
def off():
    board.digital[LED].write(0)   # Turn LED off

# Simple Controller GUI
app = tk.Tk()
app.geometry('50x50')
app.tk_setPalette('#1F1F1F')

# ON Button
tk.Button(app, text='ON', command=on).grid(row=0, column=0, padx=(22.5,5), pady=10)

#OFF Button
tk.Button(app, text='OFF', command=off).grid(row=0, column=2, padx=5, pady=10)

app.mainloop()
board.exit()