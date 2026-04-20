import  sys
from itertools import count


def main():

    stats ={
        "count": 10,
        "average": 4.5,
        "valid": True
    }
    x = stats["count"]
    print(f"{x}")
    y = stats["average"]
    print(f"{y}")
    z = stats["valid"]
    print(f"{z}")

if __name__ == "__main__":
    sys.exit(main())