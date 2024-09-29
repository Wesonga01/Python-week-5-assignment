try:
    #create and write to the file
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, my name is Wes.\n")
        file.write("Line 2: I come from Kenya.\n")
        file.write("Line 3: I am 21 years old\n")

    # Step 2: Read and display the contents
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File contents after writing:")
        print(content)

    # Step 3: Append more text
    with open("my_file.txt", "a") as file:
        file.write("Line 4: My first name is Eugene.\n")
        file.write("Line 5: I am from Western Kenya.\n")
        file.write("Line 6: Born in 2002\n")

    # Read and display the contents after appending
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File contents after appending:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
    