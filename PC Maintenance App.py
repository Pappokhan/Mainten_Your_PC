import os
#This module provides a portable way of using operating system dependent functionality. 
# If you just want to read or write a file see open(), if you want to manipulate paths, 
# see the os. path module, and if you want to read all the lines in all the files on the 
# command line see the fileinput module. For creating temporary files and directories see 
# the tempfile module, and for high-level file and directory handling see the shutil module.
import shutil
#The shutil module offers a number of high-level operations on files and collections of files. 
# In particular, functions are provided which support file copying and removal. For operations on 
# individual files, see also the os module.
import psutil
#Psutil is a Python cross-platform library used to access system details and process utilities. 
# It is used to keep track of various resources utilization in the system. Usage of resources 
# like CPU, memory, disks, network, sensors can be monitored. Hence, this library is used for 
# system monitoring, profiling, limiting process resources, and the management of running processes.

def temporary_files():
    temp= os.path.join(os.environ.get("TEMP"), "temp_folder_name")
    if os.path.exists(temp):
        try:
            shutil.rmtree(temp)
            print("Temporary files cleaned successfully...")
        except Exception as e:
            print(f"Error... Cleaning temporary files: {e}")
    else:
        print("Temporary files not found!")

def disk_space():
    total, used, free = shutil.disk_usage("/")
    print("\n---Your disk space---")
    print(f"Total Disk Space: {total / (2**30):.2f} GB")
    print(f"Used Disk Space-: {used / (2**30):.2f} GB")
    print(f"Free Disk Space-: {free / (2**30):.2f} GB")

def system_performance():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print("\n---System_performance---")
    print(f"CPU Usage---: {cpu}%")
    print(f"Memory Usage: {memory_percent}%")

def main():
    while True:
        print("\n=== Welcome PC Maintenance App ===\n")
        print("1. Clean Temporary Files!")
        print("2. Check Disk Space!")
        print("3. Monitor System Performance!")
        print("4. Exit..")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            temporary_files()
        elif choice == "2":
            disk_space()
        elif choice == "3":
            system_performance()
        elif choice == "4":
            print("\nThank You For Using Our App...\n")
            break
        else:
            print("Invalid choice...")

if __name__ == "__main__":
    main()
