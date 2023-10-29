import platform
import os

# Get the current operating system
current_os = platform.system()


def lastWord(string):
    # reversing the string
    reversed_string = string[::-1]
    # finding the index of first space in reversed string
    index = reversed_string.find(" ")
    # returning the last word in original string
    return string[-index - 1 :].replace(" ", "")


def clearScreen():
    if current_os == "Linux":
        os.system("clear")  # Clear the screen on Linux using 'clear' command
    elif current_os == "Windows":
        os.system("cls")  # Clear the screen on Windows using 'cls' command
    elif current_os == "Darwin":  # "Darwin" is the identifier for macOS
        os.system("clear")  # Clear the screen on macOS using 'clear' command
    else:
        pass
