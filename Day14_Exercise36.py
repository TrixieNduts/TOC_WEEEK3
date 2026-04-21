import sys

def main():

    #part 1
    name = input("Name: ")#askig for user input
    score1 = int(input("Enter first score: "))#asking user for input and converting to integer
    score2 = int(input("Enter second score: "))#asking user for input and converting to integer
    score3 = int(input("Enter third score: "))#asking user for input and converting to integer

    score = [score1, score2,score3]#storing user input into a list

    print(f"{score}")#thid prints the list

    #part 2
    student = {"StudentName":name, "ListOfScore":score}#creating a dict from the user input data using keys

    print(f"{student}")#this prints the dict

    #part 3
    averagescore: float = sum(score)/3#gets the score average and converts it to float

    print(f"{averagescore}")


if __name__ == "__main__":
    sys.exit(main())
