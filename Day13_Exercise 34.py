import sys

def main():

    profile = {}
    profile["name"] = input("What is your name? ")
    profile["age"] = int(input("What is your age? "))
    profile["city"] = input("What city do you reside in? ")

    print(f"{profile}")

    profile["age_next_year"] = profile["age"] + 1

    print(f"{profile}")

if __name__ == "__main__":
    sys.exit(main())


