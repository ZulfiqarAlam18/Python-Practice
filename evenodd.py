while True:
    num_input = input("Enter a number (or type 'exit' to quit): ")
    if num_input.lower() == "exit":
        print("Exiting the program.")
        break
    try:
        num = int(num_input)
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")








