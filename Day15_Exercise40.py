import sys

def main():
    settings = {"volume": 5}
    settings["volume"] = 10
    print(settings)
if __name__ == "__main__":
    sys.exit(main())