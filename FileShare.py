import pyfiglet
from colorama import Fore, Style
import tkinter as tk
from tkinter import filedialog
import qrcode 
import http.server
import socketserver
import socket
import os

root = tk.Tk()
root.withdraw()

# creating qr-Code OBJECT
qr =  qrcode.QRCode(

    version=1,  # 1 means the smallest QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border

 )


# Customize the text
name = "File - Sharer"
name1 = "          Karan-005"
big_font = pyfiglet.figlet_format(name)
bubble_font = pyfiglet.figlet_format(name1, font="bubble")

# Print the text in color
print(Fore.CYAN + big_font + Style.RESET_ALL)
print(Fore.GREEN + bubble_font + Style.RESET_ALL)



def main():
    print("Welcome to the File-Sharer")
    print("1. __Share_File__")
    # print("2. Download a file")
    print(Fore.RED + "3. __Exit__" + Style.RESET_ALL)

    choose = input("Enter the number of your choice: ")

    if choose == "1":
        folder_path = filedialog.askdirectory(title="Select a folder")
        if folder_path:
            print(f"Selected folder: {folder_path}")
            # Perform actions with the selected folder

            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            url = f"http://{local_ip}:8000/"

            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            # img.save("qr_code.png")
            img.show()
            print(f"QR code generated for: {url}")
            
            os.chdir(folder_path)  # Change directory to the one being shared
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", 8000), handler) as httpd:
                print("Press Ctrl+C to stop the server.")
                httpd.serve_forever()

            # Create a TCP/IP socket
    if choose == "3":
        print("Exiting the File-Sharer")
        print("Server Close")        
            
            



if __name__ == "__main__":
    main()            


    