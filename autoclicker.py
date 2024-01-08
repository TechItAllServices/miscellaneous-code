import time
import  threading
from pynput.mouse import Button, Controller
from pynput.keybord import listener, keycode
 

delay = 0.001
button = button.left
start_stop_key = keycode(char=’s’)
exit_key = keycode(char=’e’)

class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super(ClickMouse, self) .__init__()
		self.delay = delay
		self.button = button
		self.running = false
		self.program_running = true

def  start_clicking(self):
	self.running = true

def stop_clicking(self):
	self.running = false

def exit(self):
	self.stop_clicking()
	self.program_running = false

def run(self):
	while self.program_running:
		while self.running:
			mouse.click(self.button)
		time.sleep(0.1)

mouse
