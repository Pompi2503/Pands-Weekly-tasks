def displayMenu():
    print("what would you like to do")
    print("/t(a) Add new student")
    print("/t(v) View new student")
    print("/t(q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice
choice = displayMenu()
print(f"you chose {choice}")

