try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()

    print(data)

except FileNotFoundError as file_err:
    print("File that you are trying to open does not exist!")
    print("Error :",file_err)