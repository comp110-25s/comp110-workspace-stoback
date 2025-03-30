"""The goal is to create a program which calculates the cost of a tea party based on the # of guests"""

__author__: str = "730676777"

"""Main Function created to combine all functions"""


def main_planner(guest: int) -> None:
    print("A Cozy Tea Party for " + str(guest) + " People!")
    print("")
    print("Tea bags: " + str(tea_bags(guest)))
    print("")
    print("Treats: " + str(treats(guest)))
    print("")
    print("Cost: $" + str(cost(tea_bags(guest), treats(guest))))


"""Function created to calculate the amount of tea bags per person"""


def tea_bags(people: int) -> int:
    return people * 2


"""Function to determine the amount of treats for the entire party"""


def treats(people: int) -> int:
    return int((tea_bags(people)) * 1.5)


"""Function to determine the cost of both treats and tea for all party members"""


def cost(tea_count: int, treat_count: int) -> float:
    return float(tea_count * 0.5 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guest=int(input("How many guests are there?")))
