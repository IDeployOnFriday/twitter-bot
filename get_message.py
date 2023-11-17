def read_from_file():
    f = open("demofile.txt", "r")
    message = f.read()
    print(message)
    return message
