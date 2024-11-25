# import os
# import pyautogui
# import time
# import random
# import string
# import psutil

# # Function to generate a random 4-letter word
# def generate_random_word(length=4):
#     return ''.join(random.choices(string.ascii_lowercase, k=length))

# # Function to check if Edge is running
# def is_edge_running():
#     edge_processes = []
#     for process in psutil.process_iter(['name']):
#         if process.info['name'] and 'msedge' in process.info['name'].lower():
#             edge_processes.append(process.info['name'])
#     # Debugging: Print active Edge processes
#     print(f"Detected Edge Processes: {edge_processes}")
#     return len(edge_processes) > 0

# # Open Microsoft Edge
# application_path = "C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk"
# os.startfile(application_path)

# # Wait for the browser to open
# time.sleep(3)  # Adjust this delay if necessary

# # Perform searches while Edge is running
# print("Automation started. Close Edge to stop.")
# try:
#     while is_edge_running():
#         random_word = generate_random_word()  # Generate a random word
#         pyautogui.typewrite(random_word)     # Type the word
#         pyautogui.press('enter')             # Press Enter
#         time.sleep(8)                        # Wait for 8 seconds
# except Exception as e:
#     print(f"An error occurred: {e}")

# print("Edge closed. Automation stopped.")



import os
import pyautogui
import time
import random
import string
import keyboard  # To listen for shortcut key termination

# Function to generate a random 4-letter word
def generate_random_word(length=4):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function to automate searches in Edge
def automate_search():
    # Open Microsoft Edge
    application_path = "C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk"
    os.startfile(application_path)

    # Wait for the browser to open
    time.sleep(5)  # Adjust this delay if necessary

    print("Automation started. Press 'Ctrl+C' to stop.")

    try:
        while True:
            # Exit loop if shortcut key is pressed
            if keyboard.is_pressed("ctrl+c"):  # Terminate on Ctrl+C
                print("Termination shortcut detected. Stopping...")
                break

            # Perform the search
            random_word = generate_random_word()  # Generate a random word
            pyautogui.typewrite(random_word)     # Type the word
            pyautogui.press('enter')             # Press Enter
            time.sleep(8)                        # Wait for 8 seconds
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Automation stopped.")

if __name__ == "__main__":
    automate_search()
