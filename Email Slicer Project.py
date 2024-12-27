def main():
    print("\nWelcome to the Email Slicer!")
    print("You can slice an email to get the username, domain, and extension.")
    print("Type 'exit' at any time to quit the program.\n")

    # User input
    email_input = input("Input your email address: ").strip()

    # Exit condition
    if email_input.lower() == "exit":
        print("Thank you for using the Email Slicer. Goodbye!")
        exit()  # Ends the program

    # Splitting the email into parts
    try:
        username, domain = email_input.split("@")
        domain, extension = domain.split(".")
        
        # Displaying results
        print("\nHere are the details of your email:")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print(f"Extension: {extension}")
    except ValueError:
        print("\nInvalid email format. Please try again.")

# Continuous loop with an exit option
while True:
    main()
