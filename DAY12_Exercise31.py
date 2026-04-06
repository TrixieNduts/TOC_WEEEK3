import sys

def main():

    person = {
        "name": "Alice",
        "age": 25,
        "country": "Kenya"
    }#creates a dict with fixed data


    print(f"{person["name"]}")#prints the name
    print(f"{person["age"]}")# prints the age

if __name__ == "__main__":
    sys.exit(main())