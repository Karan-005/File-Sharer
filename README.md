# File-Sharer Program

## Overview
The **File-Sharer** program allows you to share files over your local network using an HTTP server. The program generates a QR code that can be scanned by others to access the shared folder via a web browser. It's a simple and easy way to share files without using external cloud services.

## Features 🚀
- Share files and folders over a local network.
- Generate a QR code for easy access.
- Simple and user-friendly interface using Tkinter.
- View the shared folder's content in a web browser.

## Requirements 🔧

Before running the program, make sure you have the following Python libraries installed:

1. **pyfiglet**: For displaying styled ASCII text.
2. **colorama**: For colored terminal output.
3. **qrcode**: For generating QR codes.
4. **tkinter**: For the file dialog interface (usually included by default in Python installations).
5. **http.server**: For serving the selected folder through a simple HTTP server (included in Python's standard library).
6. **socketserver**: For creating a server.

### Installation

You can install the required libraries via `pip`:

---


## How to Run 🖥️
Follow these steps to run the File-Sharer Program on your system:

## 1. Download the Program
Clone the repository or download the Python script file, for example, 'file_sharer.py', from the provided link.

## 2. Install Required Libraries
- Open the command prompt (Windows) or terminal (macOS/Linux).
- Navigate to the folder where the script is saved.
- Run the following command to install the required libraries:
      
       pip install pyfiglet colorama qrcode
       
## 3. Running the Script
To start the program, run the Python script by executing the following command in the terminal:
        
        python file_sharer.py
## 4. Program Interface
Once the script runs, it will show an ASCII title in the terminal and present a simple text-based menu:
option is not mentioned below in code because it is getting ready.....

    Welcome to the File-Sharer
    1. __Share File__
    3. __Exit__

---
## 5. Select Option 1 to Share a Folder
- When you select Option 1 (Share File), a file dialog will appear, prompting you to choose the folder you want to share.
 - Once the folder is selected, the program will:
 - Change to the directory of the selected folder.
- Generate a QR code containing a link to the shared folder (based on your local IP address).
- Start a simple HTTP server on port 8000 that serves the files in the selected folder.

---
## AUTHOR:Karan Chourasiya (Karan-005)








