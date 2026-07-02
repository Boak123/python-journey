#Task: Store Log

def write_log(message):
    with open("c:/Users/DELL/Desktop/PYTHON/log.txt", "a") as Log_file:
        bbolu = Log_file.write(message + "\n")
        print(bbolu)

write_log("This is a log message.")