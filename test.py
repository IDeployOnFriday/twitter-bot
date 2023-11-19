from main import get_post


def test_post():
    message = get_post()
    return message

if __name__ == "__main__":

    i = 1
    while i < 10:
        message = test_post()
        i += 1

    print("Everything passed")
