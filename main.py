try:
    number = 5 + "Not a number"
    # number = int("Not a number")
except ValueError:
    print("Error : Invalid value")
except TypeError:
    print("Error: Invalid type")