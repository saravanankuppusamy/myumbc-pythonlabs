#!/usr/bin/env python3


def main():
    parent1 = Person("Heather", 45, "F")
    parent2 = Person("Bill", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(parent1, parent2, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)


if __name__ == "__main__":
    main()
