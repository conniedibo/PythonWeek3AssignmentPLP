def read_and_modify_file():
    # Step 1: Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Step 4: Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: There was a problem reading the file.")

# Run the program
read_and_modify_file()
