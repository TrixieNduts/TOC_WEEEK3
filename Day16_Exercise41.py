import sys

def main():

    NAME = input("What is your name?")
    DOB = int(input("What is your birth year?"))
    COUNTRY= input("What is the name of your country?")

    dict = [NAME, DOB, COUNTRY]
    print(f"Dict = {dict}")
    new_dict = [NAME, DOB, COUNTRY]
    print(f"New_Dict = {dict}")


if __name__ == "__main__":
    sys.exit(main())