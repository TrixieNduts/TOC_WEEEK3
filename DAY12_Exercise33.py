import sys

def main():

    person = {"name": "Alice", "age": 26, "country": "Kenya"}  #creates a dict with fixed data

    person["is_student"]= False


    print(f"{person}")#prints the dict

if __name__ == "__main__":
    sys.exit(main())