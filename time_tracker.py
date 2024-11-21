
import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import os
from datetime import datetime
import time


class TimeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watch U")
        self.root.geometry("500x400")

        # Screenshot tracking variables
        self.is_tracking = False
        self.screenshot_interval = 0
        self.screenshot_thread = None
        self.stop_event = threading.Event()

        self.screenshots_dir = "my_screenshots"
        os.makedirs(self.screenshots_dir, exist_ok=True)

        self.welcome_label = tk.Label(root, text="Watching You", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=20)

        # Screenshot Interval Input
        interval_frame = tk.Frame(root)
        interval_frame.pack(pady=20)

        tk.Label(interval_frame, text="Enter Screenshot Interval (seconds):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.interval_entry = tk.Entry(interval_frame, font=("Arial", 12), width=10, justify='center')
        self.interval_entry.pack(side=tk.LEFT, padx=5)

        # Buttons Frame (shifted down)
        button_frame = tk.Frame(root)
        button_frame.pack(pady=30)

        self.clock_in_button = tk.Button(button_frame, text="Clock In", command=self.clock_in,
                                         bg="black", fg="white", font=("Arial", 14), width=15)
        self.clock_in_button.pack(side=tk.LEFT, padx=10)

        self.clock_out_button = tk.Button(button_frame, text="Clock Out", command=self.clock_out,
                                          bg="black", fg="white", font=("Arial", 14), width=15, state=tk.DISABLED)
        self.clock_out_button.pack(side=tk.LEFT, padx=10)

    def clock_in(self):
        # Get screenshot interval
        try:
            self.screenshot_interval = int(self.interval_entry.get())
            if self.screenshot_interval <= 0:
                raise ValueError("Interval must be positive")
        except (ValueError, TypeError):
            messagebox.showwarning("Input Error",
                                   "Please enter a valid screenshot interval (positive number of seconds)!")
            return

        # Start screenshot tracking
        self.is_tracking = True
        self.stop_event.clear()
        self.screenshot_thread = threading.Thread(target=self.take_continuous_screenshots)
        self.screenshot_thread.start()

        # Update UI
        messagebox.showinfo("Tracking Started", f"Started tracking with {self.screenshot_interval} second intervals")
        self.clock_in_button.config(state=tk.DISABLED)
        self.clock_out_button.config(state=tk.NORMAL)

    def take_continuous_screenshots(self):
        # Create a timestamped folder for this tracking session
        session_folder = os.path.join(
            self.screenshots_dir,
            datetime.now().strftime("%Y%m%d_%H%M%S")
        )
        os.makedirs(session_folder, exist_ok=True)

        # Take screenshots at specified interval
        screenshot_count = 0
        while not self.stop_event.is_set():
            # Take screenshot
            screenshot = pyautogui.screenshot()

            # Save screenshot with timestamp
            screenshot_filename = os.path.join(
                session_folder,
                f"screenshot_{screenshot_count:04d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            screenshot.save(screenshot_filename)

            # Increment counter
            screenshot_count += 1

            # Wait for specified interval
            time.sleep(self.screenshot_interval)

    def clock_out(self):
        # Stop screenshot tracking
        self.stop_event.set()
        if self.screenshot_thread:
            self.screenshot_thread.join()

        # Update UI
        messagebox.showinfo("Tracking Stopped", "Tracking stopped. Screenshots saved.")
        self.clock_in_button.config(state=tk.NORMAL)
        self.clock_out_button.config(state=tk.DISABLED)

        # Reset entries
        self.interval_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
app = TimeTrackerApp(root)
root.mainloop()