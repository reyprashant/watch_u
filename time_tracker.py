
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
            self.screenshot_interval = int(self.interval_entry.get()) #get the input from the user
            if self.screenshot_interval <= 0:
                raise ValueError("Interval must be positive")
        except (ValueError, TypeError):
            messagebox.showwarning("Input Error",     #fot the validation from the user and prevent the user to input the non numeric values
                                   "Please enter a valid screenshot interval (positive number of seconds)!")
            return


        self.current_session_folder = os.path.join(
            self.screenshots_dir,
            datetime.now().strftime("%Y%m%d_%H%M%S")    #generate a current folder name with the current time span
        )
        os.makedirs(self.current_session_folder, exist_ok=True)


        self.is_tracking = True #traking status to active
        self.stop_event.clear()   # to make sure that the start is fresh simply reset
        self.screenshot_thread = threading.Thread(target=self.take_continuous_screenshots) #new thread for screenshot capture
        self.screenshot_thread.start()   #start the thread


        messagebox.showinfo("Tracking Started", f"Started tracking with {self.screenshot_interval} second intervals")
        self.clock_in_button.config(state=tk.DISABLED) #diabale the clock in button so that the button is reclicked again
        self.clock_out_button.config(state=tk.NORMAL) #enable the clock out button

    def take_continuous_screenshots(self):

        screenshot_count = 0
        while not self.stop_event.is_set():   #infinite loop but when the stop event is triggered it stops

            screenshot = pyautogui.screenshot()     #most important function that takes the screen shots

            screenshot_filename = os.path.join(   #path for the screen shot
                self.current_session_folder,
                f"screenshot_{screenshot_count:04d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png" #for the unique file name
            )
            screenshot.save(screenshot_filename)   #simply saves the screenshot

            screenshot_count += 1   #next screenshot have unique value as well

            time.sleep(self.screenshot_interval)     #to take a pause from 2 screenshots

    def create_timelapse(self, screenshot_folder):    #this function creates the timelapse functions from the screenshot folder
        # Get all screenshot files
        screenshots = sorted(glob.glob(os.path.join(screenshot_folder, "screenshot_*.png")))  #this functions find all the file in the screenshot function

        if len(screenshots) < 2:
            messagebox.showwarning("Time-lapse Error", "Not enough screenshots to create time-lapse.")
            return None

        first_image = cv2.imread(screenshots[0]) #reads first screenhsot in the list
        height, width, layers = first_image.shape  # to know the picture format for the video resolution

        timelapse_path = os.path.join(screenshot_folder, "timelapse.mp4") #path where timelapse video will be saved
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') #mention the specific codec file for the video file

        frame_rate = max(1, len(screenshots) // 10) #sets the framerate based on the no of screenshots with a minimum of 1 frame per second #max(1, ...): Ensures the frame rate is at least 1 frame per second.
        out = cv2.VideoWriter(timelapse_path, fourcc, frame_rate, (width, height)) #create a video writer object with specific path, codec and framerate

        for screenshot in screenshots:
            frame = cv2.imread(screenshot)  #read the current screenshot as an image
            out.write(frame) #adds the image as a frame to the video

        out.release() #close the video writer and ensures video is saved properly

        return timelapse_path #return path to created timelapse video

    def clock_out(self):
        self.stop_event.set() #ask the thread taking screenshot to stop
        if self.screenshot_thread: #check the thread is active or not
            self.screenshot_thread.join() #waits for thread to finish execution completely before proceeding

        timelapse_path = self.create_timelapse(self.current_session_folder) #Stores the path to the created time-lapse video.

        if timelapse_path: #if the timelapse video was created sucessfully
            messagebox.showinfo("Tracking Stopped",
                                f"Tracking stopped. Screenshots saved.\n"
                                f"Time-lapse created: {timelapse_path}")
        else:
            messagebox.showinfo("Tracking Stopped", "Tracking stopped. Screenshots saved.")

        self.clock_in_button.config(state=tk.NORMAL)
        self.clock_out_button.config(state=tk.DISABLED) #allowing to clock in and disable the button

        self.interval_entry.delete(0, tk.END) #clear the input field for the next session
        self.current_session_folder = None #resets the tracking for the folder and prepare it for the next process


root = tk.Tk() #creating application root for the all gui component initializing the tkinter
app = TimeTrackerApp(root) #obj created for the TimeTrackerApp
root.mainloop() #tkinter event loop to handle ths events