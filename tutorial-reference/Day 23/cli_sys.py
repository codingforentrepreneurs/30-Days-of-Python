import sys


if __name__== "__main__":
    # test comment
    try:
        name = sys.argv[1]
    except:
        name = input("What's your name?\n")
    from getpass import getpass
    pw = getpass("What's your password?\n")
    print(name, pw)
