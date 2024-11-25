<h1>Watch U</h1>

<h3>Overview</h3>

Watch U is a Python-based desktop tool that allows users to:

Input a time for scheduled actions.

Capture screenshots.

Record data in a database.

Generate a timelapse video.

This application is built using Python and utilizes Tkinter for the graphical user interface (GUI).

<h3>Features</h3>

Time Scheduling: Input a specific time to automate actions.

Screenshot Capture: Automatically capture screenshots based on a schedule.

Data Logging: Save data into a database for later reference.

Timelapse Creation: Compile captured screenshots into a timelapse video.

<h3>Prerequisites</h3>

To run the code locally, ensure the following requirements are met:

<h5>Software Requirements</h5>

Python

Download and install Python from python.org.

<h5>Python Libraries</h5>

Install the necessary Python libraries using the following command:

pip install -r requirements.txt

The requirements.txt file contains:

PyQT5 or tkinter

OpenCV (for timelapse video creation)

Pillow (for image processing)

SQLite3 (for database operations, included in Python standard library)

PyInstaller (optional, for creating executables)


<h3>Other Dependencies</h3>

If you want to create an executable:

PyInstaller: Installed as part of the libraries.

UPX: For compressing executables (optional).


<h3>Installation and Setup</h3>

Clone the Repository

Install Dependencies

pip install -r requirements.txt

Run the Application

Execute the Python script to launch the application:
python watchu.py

<h3>Creating an Executable</h3>

To create a standalone executable for distribution:

Install PyInstaller (if not already installed):

pip install pyinstaller

Build the executable:

pyinstaller --onefile --windowed watchu.py

Locate the executable in the dist folder:
Windows: watchu.exe

Mac/Linux: watchu

<h3>Usage</h3>
Open the application.

Set a time for scheduled screenshots.

Review data saved in the database.

Export screenshots into a timelapse video.

<h3>Regarding Contributions</h3>
I welcome contributers! To contribute:

Fork the repository.
Create a new branch for your feature or bugfix.

Submit a pull request describing your changes.

<h3>Issues</h3>
If you encounter any issues, please report them in the Issues section of this repository.

<h3>Contact</h3>
For questions or support, contact:

Prashant Adhikari

Email: subash96240@gmail.com

GitHub: reyprashant
