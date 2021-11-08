import threading
import datetime
import time
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
from gi.repository import Notify

tasks = {}
class Notification:
    def __init__(self, message: str, time:str):
        self.message = message
        self.time = time

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input()) #waits to get input + Return



def get_command(inp):
    if inp == "list":
        print("/---------\\")
        for index, notification in enumerate(tasks.items()):
            print(f"{index+1}.|{notification[0]}| {notification[1]}")
        print("\---------/")
        return
    time, *message = inp.split()
    tasks[time] = " ".join(message)


def show_notification(text):
    n = Notify.Notification.new("Pytify", text)
    n.show()

keyboard = KeyboardThread(get_command)
Notify.init("Notifier")

while True:
    now = datetime.datetime.now().time()
    time_str = f"{now.hour}:{now.minute}"
    for i in tasks:
        if i == time_str:
            print("CHEEE")
            show_notification(tasks[i])
            tasks.pop(i)
            break