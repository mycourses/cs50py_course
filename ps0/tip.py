# CS50 Python 2022
# Problem Set 0 - Tip Calculator
# v1.0


def dollars_to_float(d):
    return float(d.strip("$"))


def percent_to_float(p):
    return float(p.strip("%"))


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent / 100)
    print(f"Leave ${tip:.2f}")

main()
