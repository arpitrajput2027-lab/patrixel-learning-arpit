import io

'''
else → Executes only when the try block completes without an exception.

finally → Executes whether an exception occurs or not (normally), even if the exception is not handled.

'''

try:
    fh = open("file.txt", "wt")
    fh.write("hello World !")
    fh.close()

except FileNotFoundError as file_err:
    print("File does not exist!")
    print(file_err)

except io.UnsupportedOperation as io_err:
    print(io_err)

else:
    print("else block")
    
finally:
    print("Finally block")
    fh.close()
    