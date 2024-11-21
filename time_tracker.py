#
# import tkinter as tk
# from tkinter import messagebox
# import pyautogui
# import threading
# import os
# from datetime import datetime
# import time
#
#
# class TimeTrackerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Watch U")
#         self.root.geometry("500x400")
#
#         # Screenshot tracking variables
#         self.is_tracking = False
#         self.screenshot_interval = 0
#         self.screenshot_thread = None
#         self.stop_event = threading.Event()
#
#         self.screenshots_dir = "my_screenshots"
#         os.makedirs(self.screenshots_dir, exist_ok=True)
#
#         self.welcome_label = tk.Label(root, text="Watching You", font=("Arial", 18, "bold"))
#         self.welcome_label.pack(pady=20)
#
#         # Screenshot Interval Input
#         interval_frame = tk.Frame(root)
#         interval_frame.pack(pady=20)
#
#         tk.Label(interval_frame, text="Enter Screenshot Interval (seconds):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
#         self.interval_entry = tk.Entry(interval_frame, font=("Arial", 12), width=10, justify='center')
#         self.interval_entry.pack(side=tk.LEFT, padx=5)
#
#         # Buttons Frame (shifted down)
#         button_frame = tk.Frame(root)
#         button_frame.pack(pady=30)
#
#         self.clock_in_button = tk.Button(button_frame, text="Clock In", command=self.clock_in,
#                                          bg="black", fg="white", font=("Arial", 14), width=15)
#         self.clock_in_button.pack(side=tk.LEFT, padx=10)
#
#         self.clock_out_button = tk.Button(button_frame, text="Clock Out", command=self.clock_out,
#                                           bg="black", fg="white", font=("Arial", 14), width=15, state=tk.DISABLED)
#         self.clock_out_button.pack(side=tk.LEFT, padx=10)
#
#     def clock_in(self):
#         # Get screenshot interval
#         try:
#             self.screenshot_interval = int(self.interval_entry.get())
#             if self.screenshot_interval <= 0:
#                 raise ValueError("Interval must be positive")
#         except (ValueError, TypeError):
#             messagebox.showwarning("Input Error",
#                                    "Please enter a valid screenshot interval (positive number of seconds)!")
#             return
#
#         # Start screenshot tracking
#         self.is_tracking = True
#         self.stop_event.clear()
#         self.screenshot_thread = threading.Thread(target=self.take_continuous_screenshots)
#         self.screenshot_thread.start()
#
#         # Update UI
#         messagebox.showinfo("Tracking Started", f"Started tracking with {self.screenshot_interval} second intervals")
#         self.clock_in_button.config(state=tk.DISABLED)
#         self.clock_out_button.config(state=tk.NORMAL)
#
#     def take_continuous_screenshots(self):
#         # Create a timestamped folder for this tracking session
#         session_folder = os.path.join(
#             self.screenshots_dir,
#             datetime.now().strftime("%Y%m%d_%H%M%S")
#         )
#         os.makedirs(session_folder, exist_ok=True)
#
#         # Take screenshots at specified interval
#         screenshot_count = 0
#         while not self.stop_event.is_set():
#             # Take screenshot
#             screenshot = pyautogui.screenshot()
#
#             # Save screenshot with timestamp
#             screenshot_filename = os.path.join(
#                 session_folder,
#                 f"screenshot_{screenshot_count:04d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
#             )
#             screenshot.save(screenshot_filename)
#
#             # Increment counter
#             screenshot_count += 1
#
#             # Wait for specified interval
#             time.sleep(self.screenshot_interval)
#
#     def clock_out(self):
#         # Stop screenshot tracking
#         self.stop_event.set()
#         if self.screenshot_thread:
#             self.screenshot_thread.join()
#
#         # Update UI
#         messagebox.showinfo("Tracking Stopped", "Tracking stopped. Screenshots saved.")
#         self.clock_in_button.config(state=tk.NORMAL)
#         self.clock_out_button.config(state=tk.DISABLED)
#
#         # Reset entries
#         self.interval_entry.delete(0, tk.END)
#
#
# # Create the main window
# root = tk.Tk()
# app = TimeTrackerApp(root)
# root.mainloop()

import tkinter as tk #for gui
from tkinter import messagebox #for pop up messages
import pyautogui #for screenshots
import threading #for taking screenshots at background without any lag
import os #to create the necessary files and folders
import cv2 #opencv library to create the timelapse video
import numpy as np # numpy for the array access and also for the math functions
from datetime import datetime #for generating time stamps for naming files and folders
import time # to add delay between the screen shots
import glob #this is used to find the files with a similar pattern for this it is used for geetung the screenshot files


class TimeTrackerApp:
    def __init__(self, root): #constructor innitiated for gui it is used to refer to the window
        self.root = root
        self.root.title("Watch U") #setting title
        self.root.geometry("500x400") #setting size of the window

#main variables
        self.is_tracking = False #indicates whether the screen shot is on or not or the process is on or not
        self.screenshot_interval = 0 #indicating the interval of the time gap between the intervals
        self.screenshot_thread = None #for taking screenshots in background
        self.stop_event = threading.Event() #stopping the thread
        self.current_session_folder = None #where current screenshot is saved

        self.screenshots_dir = "my_screenshots"
        os.makedirs(self.screenshots_dir, exist_ok=True)  #make directory to save all the screenshots

        self.welcome_label = tk.Label(root, text="Watching You", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=20)# for the label parameter pady refers to the padding from the element on each side


        interval_frame = tk.Frame(root)
        interval_frame.pack(pady=20)

        tk.Label(interval_frame, text="Enter Screenshot Interval (seconds):", font=("Arial", 12)).pack(side=tk.LEFT,
                                                                                                       padx=5)
        self.interval_entry = tk.Entry(interval_frame, font=("Arial", 12), width=10, justify='center')
        self.interval_entry.pack(side=tk.LEFT, padx=5) #for the label and user to enter the  interval time


        button_frame = tk.Frame(root) #Creates a new frame and assigns it to the button_frame variable. The root argument specifies that this frame is a child of the root window.
        button_frame.pack(pady=30) #pack or simply put the button_frame variable into the root window

        self.clock_in_button = tk.Button(button_frame, text="Clock In", command=self.clock_in,
                                         bg="black", fg="white", font=("Arial", 14), width=15)
        self.clock_in_button.pack(side=tk.LEFT, padx=10)

        self.clock_out_button = tk.Button(button_frame, text="Clock Out", command=self.clock_out,
                                          bg="black", fg="white", font=("Arial", 14), width=15, state=tk.DISABLED)
        self.clock_out_button.pack(side=tk.LEFT, padx=10)  #for clockin and clock out button

    def clock_in(self):

        try:
            self.screenshot_interval = int(self.interval_entry.get())
            if self.screenshot_interval <= 0:
                raise ValueError("Interval must be positive")
        except (ValueError, TypeError):
            messagebox.showwarning("Input Error",
                                   "Please enter a valid screenshot interval (positive number of seconds)!")
            return


        self.current_session_folder = os.path.join(
            self.screenshots_dir,
            datetime.now().strftime("%Y%m%d_%H%M%S")
        )
        os.makedirs(self.current_session_folder, exist_ok=True)


        self.is_tracking = True
        self.stop_event.clear()
        self.screenshot_thread = threading.Thread(target=self.take_continuous_screenshots)
        self.screenshot_thread.start()


        messagebox.showinfo("Tracking Started", f"Started tracking with {self.screenshot_interval} second intervals")
        self.clock_in_button.config(state=tk.DISABLED)
        self.clock_out_button.config(state=tk.NORMAL)

    def take_continuous_screenshots(self):

        screenshot_count = 0
        while not self.stop_event.is_set():

            screenshot = pyautogui.screenshot()

            screenshot_filename = os.path.join(
                self.current_session_folder,
                f"screenshot_{screenshot_count:04d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            screenshot.save(screenshot_filename)

            screenshot_count += 1

            time.sleep(self.screenshot_interval)

    def create_timelapse(self, screenshot_folder):
        # Get all screenshot files
        screenshots = sorted(glob.glob(os.path.join(screenshot_folder, "screenshot_*.png")))

        if len(screenshots) < 2:
            messagebox.showwarning("Time-lapse Error", "Not enough screenshots to create time-lapse.")
            return None

        first_image = cv2.imread(screenshots[0])
        height, width, layers = first_image.shape

        timelapse_path = os.path.join(screenshot_folder, "timelapse.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        frame_rate = max(1, len(screenshots) // 10)
        out = cv2.VideoWriter(timelapse_path, fourcc, frame_rate, (width, height))

        for screenshot in screenshots:
            frame = cv2.imread(screenshot)
            out.write(frame)

        out.release()

        return timelapse_path

    def clock_out(self):
        self.stop_event.set()
        if self.screenshot_thread:
            self.screenshot_thread.join()

        timelapse_path = self.create_timelapse(self.current_session_folder)

        if timelapse_path:
            messagebox.showinfo("Tracking Stopped",
                                f"Tracking stopped. Screenshots saved.\n"
                                f"Time-lapse created: {timelapse_path}")
        else:
            messagebox.showinfo("Tracking Stopped", "Tracking stopped. Screenshots saved.")

        self.clock_in_button.config(state=tk.NORMAL)
        self.clock_out_button.config(state=tk.DISABLED)

        self.interval_entry.delete(0, tk.END)
        self.current_session_folder = None


root = tk.Tk()
app = TimeTrackerApp(root)
root.mainloop()