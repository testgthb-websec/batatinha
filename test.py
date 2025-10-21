option = 0
while True:
    print("Menu:")
    print("1. soma 1")
    print("2. subtração 2")
    print("3. Exit")
    try:
        option = int(input("Select an option (1-3): "))
        if option == 1:
            print("You selected Option 1.")
        elif option == 2:
            print("You selected Option 2.")
        elif option == 4:
            print("You selected Option 4.")
        elif option == 5 :
            print("You selected Option 5.")
        elif option == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")