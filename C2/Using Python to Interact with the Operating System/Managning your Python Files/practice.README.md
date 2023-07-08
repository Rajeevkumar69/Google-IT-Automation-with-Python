Practice Notebook: Reading and Writing Files
In this exercise, we will test your knowledge of reading and writing files by playing around with some text files.

Let's say we have a text file containing current visitors at a hotel. We'll call it, guests.txt. Run the following code to create the file. The file will automatically populate with each initial guest's first name on its own line.

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
​
for i in initial_guests:
guests.write(i + "\n")

guests.close()
No output is generated for the above code cell. To check the contents of the newly created guests.txt file, run the following code.

with open("guests.txt") as guests:
for line in guests:
print(line)
The output shows that our guests.txt file is correctly populated with each initial guest's first name on its own line. Cool!

Now suppose we want to update our file as guests check in and out. Fill in the missing code in the following cell to add guests to the guests.txt file as they check in.

new\*guests = ["Sam", "Danielle", "Jacob"]
​
with open("guests.txt", \*\**) as guests:
for i in new*guests:
guests.\*\*\*(i + "\n")
​
guests.close()
To check whether your code correctly added the new guests to the guests.txt file, run the following cell.

with open("guests.txt") as guests:
for line in guests:
print(line)
Bob

Andrea

Manuel

Polly

Khalid

The current names in the guests.txt file should be: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.

Was the guests.txt file correctly appended with the new guests? If not, go back and edit your code making sure to fill in the gaps appropriately so that the new guests are correctly added to the guests.txt file. Once the new guests are successfully added, you have filled in the missing code correctly. Great!

Now let's remove the guests that have checked out already. There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:

Open the file in "read" mode.
Iterate over each line in the file and put each guest's name into a Python list.
Open the file once again in "write" mode.
Add each guest's name in the Python list to the file one by one.

Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]
​
with open("guests.txt", "r" ) as guests:
for g in guests:
temp_list.append(g.strip())
​
with open("guests.txt", "w" ) as guests:
for name in temp_list:
if name not in checked_out:
guests.write(name + "\n")
To check whether your code correctly removed the checked out guests from the guests.txt file, run the following cell.

with open("guests.txt") as guests:
for line in guests:
print(line)
Bob

Andrea

Manuel

Polly

Khalid

The current names in the guests.txt file should be: Bob, Polly, Sam, Danielle and Jacob.

Were the names of the checked out guests correctly removed from the guests.txt file? If not, go back and edit your code making sure to fill in the gaps appropriately so that the checked out guests are correctly removed from the guests.txt file. Once the checked out guests are successfully removed, you have filled in the missing code correctly. Awesome!

Now let's check whether Bob and Andrea are still checked in. How could we do this? We'll just read through each line in the file to see if their name is in there. Run the following code to check whether Bob and Andrea are still checked in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []
​
with open("guests.txt","r") as guests:
for g in guests:
checked_in.append(g.strip())
for check in guests_to_check:
if check in checked_in:
print("{} is checked in".format(check))
else:
print("{} is not checked in".format(check))
Bob is checked in
Andrea is checked in
We can see that Bob is checked in while Andrea is not. Nice work! You've learned the basics of reading and writing files in Python!

The current names in the guests.txt file should be: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.

Was the guests.txt file correctly appended with the new guests? If not, go back and edit your code making sure to fill in the gaps appropriately so that the new guests are correctly added to the guests.txt file. Once the new guests are successfully added, you have filled in the missing code correctly. Great!

Now let's remove the guests that have checked out already. There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:

Open the file in "read" mode.
Iterate over each line in the file and put each guest's name into a Python list.
Open the file once again in "write" mode.
Add each guest's name in the Python list to the file one by one.

Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r" ) as guests:
for g in guests:
temp_list.append(g.strip())

with open("guests.txt", "w" ) as guests:
for name in temp_list:
if name not in checked_out:
guests.append(name + "\n")

correct thios code

ChatGPT
There is a small error in the code you provided. Instead of using guests.append(name + "\n"), you should use guests.write(name + "\n") to write each guest's name to the file. Here's the corrected code:

python
Copy code
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
for g in guests:
temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
for name in temp_list:
if name not in checked_out:
guests.write(name + "\n")
This code will open the guests.txt file in read mode and iterate over each line, adding each guest's name to the temp_list after stripping any leading or trailing whitespace. Then it opens the file again in write mode and writes each guest's name to the file, excluding the ones in the checked_out list. Each name is written with a newline character "\n" appended to it to separate the names on different lines.

User
def create\*python_script(filename):
comments = "# Start of a new Python program"
with \*\*\*:
filesize = \_\*\*
return(filesize)

print(create_python_script("program.py"))
fill iun the gap to create "script.py
ChatGPT
To create a Python script named "script.py" and determine its file size, you can use the following code:

python
Copy code
def create_python_script(filename):
comments = "# Start of a new Python program"
with open(filename, "w") as script:
script.write(comments)
filesize = 0
with open(filename, "r") as script:
filesize = len(script.read())
return filesize

print(create_python_script("script.py"))
In the code above, the create_python_script function takes a filename parameter and writes the comments to the specified file using open with the mode set to "w" (write mode). The with statement ensures that the file is properly closed after writing.

Afterward, the function opens the file in read mode ("r"), reads its contents using script.read(), and assigns the length of the content to the filesize variable. Finally, the function returns the filesize.

The print statement at the end calls the create_python_script function, passing "script.py" as the filename argument, and prints the resulting filesize value.

User
import os

def new_directory(directory, filename):

# Before creating a new directory, check to see if it already exists

if os.path.isdir(directory) == False:
\_\_\_

# Create the new file inside of the new directory

os.chdir(**_)
with open (_**) as file:
pass

# Return the list of files in the new directory

return \_\_\_

print(new_directory("PythonPrograms", "script.py"))
fill iun the gap to create "script.py " in the directory "pythonProgram"
ChatGPT
To create a new directory named "PythonPrograms" and a file named "script.py" inside that directory using the new_directory function, you can fill in the gaps in the code as follows:

python
Copy code
import os

def new_directory(directory, filename): # Before creating a new directory, check to see if it already exists
if os.path.isdir(directory) == False:
os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
In the code above, the new_directory function takes two parameters: directory (the name of the new directory) and filename (the name of the file to create inside the new directory).

First, the function checks if the directory already exists using os.path.isdir(directory). If it doesn't exist, the function creates the directory using os.mkdir(directory).

Next, it changes the current working directory to the newly created directory using os.chdir(directory).

Then, it creates the new file inside the new directory using open(filename, "w"). The "w" mode specifies that the file should be opened in write mode.

Afterward, the function returns the list of files in the new directory using os.listdir().

Finally, the print statement calls the new_directory function with "PythonPrograms" as the directory argument and "script.py" as the filename argument. It prints the resulting list of files in the new directory.

User
import os
import datetime

def file_date(filename):

# Create the file in the current directory

---

timestamp = \_\_\_

# Convert the timestamp into a readable format, then into a string

---

# Return just the date portion

# Hint: how many characters are in “yyyy-mm-dd”?

return ("{**_}".format(_**))

print(file_date("newfile.txt"))

# Should be today's date in the format of yyyy-mm-dd

fill in the blank to create the file called "newfile.txt" and check the date it was modified
ChatGPT
To create the file "newfile.txt" and check the date it was last modified using the file_date function, you can fill in the blanks as follows:

python
Copy code
import os
import datetime

def file_date(filename): # Create the file in the current directory
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

In the code above, the file_date function takes a filename parameter.

First, it creates the file "newfile.txt" in the current directory using open(filename, "w") within a with statement. This ensures that the file is properly closed after creation.

Next, it retrieves the timestamp of the file's last modification using os.path.getmtime(filename). This timestamp represents the number of seconds since the epoch.

Then, it converts the timestamp into a readable format by creating a datetime.datetime object from the timestamp and using strftime to format it as "%Y-%m-%d", representing the year, month, and day.

Finally, it returns the formatted date as a string.

The print statement calls the file_date function with "newfile.txt" as the filename argument and prints the resulting date, which should be today's date in the format "yyyy-mm-dd".

User
import os
def parent_directory():

# Create a relative path to the parent

# of the current working directory

relative\*parent = os.path.join(\*\*\*, \_\*\*)

# Return the absolute path of the parent directory

return \_\_\_

print(parent_directory())

fill in the blank
ChatGPT
To fill in the blanks in the code and create a function parent_directory() that returns the absolute path of the parent directory of the current working directory, you can use the following code:

python
Copy code
import os

def parent_directory(): # Create a relative path to the parent # of the current working directory
relative_parent = os.path.join(os.getcwd(), os.pardir)

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())
In the code above, the parent_directory function uses os.getcwd() to get the current working directory and os.pardir to represent the parent directory.

The os.path.join() function is used to create a relative path by combining the current working directory and the parent directory.

Then, os.path.abspath() is used to get the absolute path of the parent directory by converting the relative path to an absolute path.

Finally, the print statement calls the parent_directory function and prints the resulting absolute path of the parent directory.
