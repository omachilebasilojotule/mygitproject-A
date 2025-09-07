#python week 4 assignment
from inspect import getfile


open("original.txt", "r")
any
content = any.read()
modified_content = content.upper()
open("modified.txt", "w")
getfile
getfile.write(modified_content)
print("file modified and saved as 'modified.txt'.")
FileNotFoundError
print("the file 'original.txt' was not found.")

#ask the user for file name
filename = input("Enter the name of the file to read:")
getfile
open(filename, "r")
data = getfile.read()
print("file content:\n", data)
FileNotFoundError
print("Error: file not found.")




