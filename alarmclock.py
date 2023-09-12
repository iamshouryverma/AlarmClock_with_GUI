import threading
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
import winsound  # Required for sound on Windows
import threading  # Import the threading module

# ... (rest of your code)

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
import winsound  # Required for sound on Windows

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # Create and configure GUI widgets
        self.label = ttk.Label(root, text="Set Alarm Time (HH:MM AM/PM):")
        self.label.pack(pady=10)

        self.alarm_time_entry = ttk.Entry(root)
        self.alarm_time_entry.pack(pady=5)

        self.set_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=5)

        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=10)

        self.activate_button = ttk.Button(root, text="Activate Alarm", command=self.activate_alarm)
        self.activate_button.pack(pady=5)

        self.deactivate_button = ttk.Button(root, text="Deactivate Alarm", command=self.deactivate_alarm)
        self.deactivate_button.pack(pady=5)
        self.deactivate_button["state"] = "disabled"  # Initially disabled

        # Initialize alarm properties
        self.alarm_time = None
        self.alarm_active = False

    def set_alarm(self):
        alarm_time_str = self.alarm_time_entry.get()
        try:
            self.alarm_time = datetime.strptime(alarm_time_str, "%I:%M %p")
            self.status_label["text"] = f"Alarm set for {self.alarm_time.strftime('%I:%M %p')}"
        except ValueError:
            self.status_label["text"] = "Invalid time format (HH:MM AM/PM)"

    def activate_alarm(self):
        if self.alarm_time and not self.alarm_active:
            self.alarm_active = True
            self.activate_button["state"] = "disabled"
            self.deactivate_button["state"] = "active"
            alarm_thread = threading.Thread(target=self.check_alarm)
            alarm_thread.start()

    def deactivate_alarm(self):
        self.alarm_active = False
        self.activate_button["state"] = "active"
        self.deactivate_button["state"] = "disabled"
        self.status_label["text"] = ""

    def check_alarm(self):
        while self.alarm_active:
            current_time = datetime.now().strftime("%I:%M %p")
            if current_time == self.alarm_time.strftime("%I:%M %p"):
                self.status_label["text"] = "Alarm activated!"
                self.activate_button["state"] = "active"
                self.deactivate_button["state"] = "disabled"
                self.play_alarm_sound()
                self.alarm_active = False
            time.sleep(60)  # Check every minute

    def play_alarm_sound(self):
        try:
            winsound.Beep(1000, 1000)  # Play a simple beep sound (Windows only)
        except Exception as e:
            print(f"Failed to play sound: {e}")

def main():
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
