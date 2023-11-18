import randon

greetings = [
    "Good Morning ",
    "Happy Morning",
    "What's up?",
    "How's it going?"
]



def read_from_file():
    f = open("demofile.txt", "r")
    message = f.read()
    print(message)
    return message

def get_greeting():
    greeting = randon.choice(greetings)
    return greeting

def get_body():
    return "no bug day "
def get_hashtags():
    return "#devs"


