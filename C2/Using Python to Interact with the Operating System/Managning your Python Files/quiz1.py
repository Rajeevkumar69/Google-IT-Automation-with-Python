# Q1. Solution
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# Q2. Solution
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as script:
        script.write(comments)
    filesize = 0
    with open(filename, "r") as script:
        filesize = len(script.read())
    return filesize

print(create_python_script("script.py"))

# Q3. Solution
import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

# Q4. Solution
import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass

    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date_modified = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return date_modified

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
