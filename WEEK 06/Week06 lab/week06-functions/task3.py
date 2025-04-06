def displayMenu():
    print("what would you like to do")
    print("/t(a) Add new student")
    print("/t(v) View new student")
    print("/t(q) Quit")
    choice = input("Type one letter (a/v/q)").strip()
    return choice
def doAdd():
    print("in adding")
def doView():
    print("in Viewing")
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'a':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
choice=displayMenu()