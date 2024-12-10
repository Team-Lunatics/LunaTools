def say(message):
    print(message)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python say.py <message>")
    else:
        message = " ".join(sys.argv[2:])
        say(message)
