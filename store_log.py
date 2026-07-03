#Task: Store Log
import os

# def write_log(message):
#     with open("c:/Users/DELL/Desktop/PYTHON/log.txt", "a") as Log_file:
#         bbolu = Log_file.write(message + "\n")
#         print(bbolu)

# write_log("This is a log message.")


# with open("c:/Users/DELL/Desktop/PYTHON/log.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("c:/Users/DELL/Desktop/PYTHON/log.txt", "r") as f:
#   print(f.read())

#f = open("myfile.txt", "x")



if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
  print("File deleted successfully.")
else:
  print("The file does not exist.")