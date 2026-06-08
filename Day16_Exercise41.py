import sys

def main():

    NAME = input("What is your name?")
    DOB = input(int("What is your birth year?"))
    COUNTRY= input("What is the name of your country?")

    dict = [NAME, DOB, COUNTRY]
    print(f"{dict}")
if __name__ == "__main__":
    sys.exit(main())