# Facial Recognition Attendance Program
### Project: Scientific Research Project at Hanoi University of Architecture

## Program Overview:
This program utilizes facial recognition technology to automate student attendance tracking. It is designed for use in educational settings to streamline attendance management and reduce the administrative burden of manual attendance recording.
## Key Features:
  - Facial Recognition: Leverages facial recognition algorithms to identify and verify student identities, ensuring accurate attendance records.
  - Automated Attendance Tracking: Automatically marks attendance for students upon successful facial recognition, eliminating the need for manual sign-ins or punch cards.
  - Data Management: Stores attendance data in a secure database, enabling easy access to attendance records for analysis and reporting purposes.
## Program Requirements:
  - Python 3.10.11 or 3.9: The program requires a specific version of Python to function correctly.
  - GTK3 runtime Win64: An essential runtime environment is needed for the program to run on Windows 64-bit systems.
## Program Execution:
  - Install Python 3.10.11 or 3.9: Ensure that the specified Python version is installed on the system.
  - Install GTK3 runtime Win64: Install the GTK3 runtime Win64 to enable the program to run on the system.
  - Run Setup.exe: Execute the Setup.exe file to install the required libraries and dependencies for the program.
  - Launch App.exe: Once the setup process is complete, run the App.exe file to start the facial recognition attendance program.
## Program Structure:
The program's structure is organized into the following directories:
  - hau_haar: Contains the Haar model utilized for facial recognition.
  - hau_main: Houses the main program files:
    main_login: Handles user login and authentication.
    main_admin: Provides administrative functionalities.
    main_attendance: Manages the attendance recording process.
    main_importer: Imports necessary libraries for the program.
  - hau_modules: Contains various program modules:
    + hau_collector: Establishes the program's structure, including data and file management.
    + hau_datasupportor: Handles loading image data.
    + hau_importer: Imports required libraries.
    + hau_model: Constructs the Convolutional Neural Network (CNN) model.
  - hau_settings: Defines constant variables.
  - hau_thread: Runs video processing in the background.
  - hau_setup: Includes setup files, requirements.txt, and run.
  - hau_ui: Contains files related to building the program's user interface.
  - resources: Houses icons and links icons to PyQt5.
## Additional Notes:
  - The program is designed for use in educational settings with controlled lighting conditions and adequate face detection capabilities.
  - For optimal performance, ensure that the camera used for facial recognition is properly positioned and calibrated.
  - The program's accuracy may be affected by factors such as facial expressions, occlusions, and low-quality lighting conditions.
## Disclaimer:
This program is provided for research and educational purposes only. It is not intended for commercial use or deployment in critical applications. Further development and refinement may be necessary to ensure its suitability for real-world scenarios.
