# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"
my_file = "week-03/day-01/my-file.txt"
def line_printer(file_name):
    try:
        file = open(file_name, "r")
        for line in file:
            print(line)
        file.close()
    except IOError:
        print("Unable to read file: " + file_name)
line_printer(my_file)