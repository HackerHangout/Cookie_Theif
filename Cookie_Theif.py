# Cookie Theif

# Imports

import subprocess

import time

import os

# varibles

logo = """
                 _    _           
                | |  (_)          
  ___ ___   ___ | | ___  ___  
 / __/ _ \ / _ \| |/ / |/ _ |
| (_| (_) | (_) |   <| |  __/
 \___\___/ \___/|_|\_\_|\___|

 _   _     _       __ 
| | | |   (_)     / _|
| |_| |__  _  ___| |_ 
| __| '_ \| |/ _ \  _|
| |_| | | | |  __/ |  
 \__|_| |_|_|\___|_|  
    [BY: HackerHangout]           
"""

# start up

print(logo)

time.sleep(3)

print("Starting Cookie Theif...")

time.sleep(1.5)


def shoot():
    print("Starting Server... ")

    time.sleep(3)

    os.system("clear")

    try:

        print(logo)

        print("-----<Server Started>-----")

        print("Waiting For Cookies")

        subprocess.call("python3 -m http.server 8080", shell=True)

        # waiting for cookies!

    except KeyboardInterrupt:

        ask = input("\n Do You Want To Close 'Cookie Theif'?...(Y/N)")

        if ask == 'Y':

            print("Closing 'Cookie Theif'...")

            time.sleep(3)

            exit()

        elif ask == 'N':

            pass

        else:

            print("What The Fuck Was That.")

            time.sleep(1.5)

            print("I'm Leaving")

            time.sleep(1.5)

            print("Bye Piece Of Shit!")

            time.sleep(1.5)

            exit()


def main():

    shoot()

main()
