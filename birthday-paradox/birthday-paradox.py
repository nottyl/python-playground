"""
My implementation of birthday paradox by Al Sweigart
"""

import datetime
import random


def main():
    print("The Birthday Paradox (Not actually a paradox though)")
    print("This program uses a Monte Carlo simulation to count that in a group of n people,")
    print("the odds of two people having the same birthday is actually pretty large.")

    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    # Keep executing until the user enters a valid input
    while True:
        print("How many birthdays to be generated? (Max: 100)")
        response = input("> ")
        if response.isdecimal() and (0 < int(response) <= 100):
            birthdayAmount = int(response)
            break

    print()

    print("Here are", birthdayAmount, "birthdays:")
    birthdays = getBirthdays(birthdayAmount)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # Print comma after the first birthday
            print(", ", end='')
        month = MONTHS[birthday.month-1]
        dateStr = "{} {}".format(month, birthday.day)
        print(dateStr, end="")

    print()
    print()

    match = getMatch(birthdays)

    print("In this simulation, ", end="")
    if match != None:
        month = MONTHS[match.month-1]
        dateStr = "{} {}".format(month, birthday.day)
        print("Multiple people have a birthday on", dateStr)
    else:
        print("There are no matching birthdays")

    print()

    simulation(birthdayAmount)


def getBirthdays(birthdayNums):
    birthdays = []
    for i in range(birthdayNums):
        year = datetime.date(2002, 1, 1)

        randomDays = datetime.timedelta(random.randint(0, 364))
        birthday = year + randomDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, birthdayI in enumerate(birthdays):
        for j, birthdayJ in enumerate(birthdays[i+1]):
            if birthdayI == birthdayJ:
                return birthdayI


def simulation(birthdayNums):
    print("Generating", birthdayNums, "random birthday 100,000 times:")
    input("Press enter to begin...")
    simMatch = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, "simulations completed...")
        birthdays = getBirthdays(birthdayNums)
        if getMatch(birthdays) != None:
            simMatch += 1
    print("Simulation finished")

    # Results
    prob = round(simMatch / 100_000 * 100, 2)
    print("Out of 100,000 simulations of", birthdayNums, "people, there was a")
    print("matching birthday in that group", simMatch, "times. This means that")
    print(birthdayNums, "people have a", prob, "chance of having a matching birthday.")
