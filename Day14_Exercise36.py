import sys

def main():

    name = input("Name: ")
    score1 = int(input("Enter first score: "))
    score2 = int(input("Enter second score: "))
    score3 = int(input("Enter third score: "))

    score = [score1, score2,score3]

    print(f"{score}")

    student = {"StudentName":name, "ListOfScore":score}

    print(f"{student}")


if __name__ == "__main__":
    sys.exit(main())
