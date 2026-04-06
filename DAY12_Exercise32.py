import sys

def main():

    person = {
        "name": "Alice",
        "age": 25,
        "country": "Kenya"
    }#creates a dict with fixed data

    person["age"] = 26#assignes a new value to age
    print(f"{person}")#prints the dict

if __name__ == "__main__":
    sys.exit(main())