import os
import sys
import time
import threading
from process_email_file import Process

filter = {
}

def load_filter():
    with open(path_setting, 'r',encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split(';')
            filter[key] = value

def rename_msg_files(path):
    threads = []
    lock = threading.Lock()
    start_time = time.time()
    process_file = Process(path,filter)
    for file in os.listdir(path):
        if file.endswith(".msg") | file.endswith(".eml") :
            thread = threading.Thread(target=process_file.rename_email_file, args=(file,lock))
            thread.start()
            threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Tous les fichiers MSG ont été renommés avec succès.")
    elapsed_time = end_time - start_time
    print(f"Timer: {elapsed_time} seconds")


if len(sys.argv) > 1 :
    path = sys.argv[1]
    path_setting = path+'\setting.txt'
    path = path+"\email"
    load_filter()
    print("File path:", path)
    rename_msg_files(path)
else:
    print("Please provide a file path as a command-line argument.")
