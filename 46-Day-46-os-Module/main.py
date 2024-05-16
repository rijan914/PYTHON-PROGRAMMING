# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

# import os 

# if (not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,10):
#     os.mkdir(f"data/Day{i+1}")
    
#for renaming 
# for i in range(0,10 ):
#     os.rename(f"data/Tutorial{i+1}",f"data/Tutorial{i+1}")

# folders=os.listdir("data")
# print(folders)
# #open the field in read only mode 
# f = os.open("myfile.txt", os.O_RDONLY)
# # Read the contents of the file
# contents = os.read(f, 1024)
# # Close the file
# os.close(f)
# print(os.getcwd())
# os.rmdir("data")

# import os

# # Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)

# # Read the contents of the file
# contents = os.read(f, 1024)

# # Close the file
# os.close(f)

# To open a file for writing, you can use the os.O_WRONLY flag:

# import os
# # Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)
# # Write to the file
# os.write(f, b"Hello, world!")
# # Close the file
# os.close(f)

# Interacting with the file system
# The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory:

# import os
# # Get a list of the files in the current directory
# files = os.listdir(".")
# print(files)  # Output: ['myfile.txt', 'otherfile.txt']


# import os
# # Create a new directory
# os.mkdir("newdir")

# import os
# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# import os
# # Run the "ls" command and get the output as a file-like object
# f = os.popen("ls")
# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# # Close the file-like object
# f.close()
