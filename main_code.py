#!/usr/bin/env python3
import os 
import subprocess


# send_mail function
def send_message(recipient, subject, body):
    try:
      process = subprocess.Popen(['mail', '-a', 'Content-type: text/html;', '-s', subject, recipient],
                               stdin=subprocess.PIPE)
    except Exception as e:
      print(e)
    process.communicate(body)

# address, unique text, file name
def grab_update_text(recipient, subject, find_text, update_text, anchor_link, file_name):
    
    # Get current path of that file
    dir_path_file = os.path.dirname(os.path.realpath(__file__)) + '/' + file_name +'.txt'

    # If findWord is found
    if find_text.search(update_text):
        # Converting body message from string to byte so that mail command can accept that 
        body = bytes(f"<a href='{anchor_link}'>{update_text}</a>", encoding='utf-8')
    # If file exist
        if os.path.isfile(dir_path_file):
    # Open the file for read
            f = open(dir_path_file, 'r')
            # print(f.readlines()[-1].strip('\n'))  #Read all the lines and return last line only
            # If update not exist, add the new update text to file and send email 
            if f.readline().strip('\n') != update_text:
                with open(dir_path_file, 'w') as file:
                    file.write(update_text)         
                send_message(recipient, subject, body)
                # subprocess.call(emailCmd.split())
                # file.write("\n")    
                print('file updated')
            print('No new update')

    # If file not exist, create file, add the new update text to file and send email 
        else:
            with open(dir_path_file, 'w') as file:
                file.write(update_text)
            print('file created')
            send_message(recipient, subject, body)
            # subprocess.call(emailCmd.split())
            # file.write("\n")

