file = open("spider.txt")
print(file.readline())

print(file.readline())

print(file.read())

# open-use-close file
file.close() 

# Python automatically close the file
with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())

# To remove the New line character
with open("spider.txt") as file:
    for line in file:
        print(line.strip())

# Open file "spider.txt", read all lines into a list, close file, print list.
file = open("spider.txt")
lines = file.readlines()
file.close()
print(lines)

# Writing Files

with open("spider.txt") as file:
    file.write("Hello chamchamG")

# Working with Files

# Remove the File
import os
os.remove("spider.txt")

# Rename the file
os.rename("ab.txt","chamcham.txt")

# It'll return boolean value --> if exist True else return false
os.path.exists("ab.txt")

#More File Information

# To check the file size
os.path.getsize("spider.txt")

#It represent the number of seconds
os.path.getmtime("spider.txt")

import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)

# It return the absoulate path
os.path.abspath("spider.txt")

# Directories
print(os.getcwd())

#  Create the directories
os.mkdir("new_dir")

# Change the directories
os.chdir("new_dir")

# Remove directories
os.rmdir("new_dir")

# Return the list of the file in this directories
os.listdir("website")

# This code iterates through the contents of the directory "website" and prints whether each item is a file or a directory.
dir = "website"
for name in os.listdir(dir):
    fullName = os.path.join(dir,name)
    if os.path.isdir(fullName):
        print("{} is a directory".format(fullName))
    else:
        print("{} is a file".format(fullName))

# CSV File

import csv
f = open("spider.txt")
csv_f = csv.reader(f)

# Iterate through this csv file
import csv
f = open("spider.txt")
csv_f = csv.reader(f)
for row in csv_f:
        # Unpack the Data
    name,phone,role = row
#      Print the Unpacked Data
    print("Name: {}","Phone {}","Role {}")
# Close the file
f.close()


# Store the Data in CSV file
hosts = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]
with open('host.csv','w') as hosts_csv:
    write = csv.writer(hosts_csv)
    write.writerows(hosts)

with open('software.csv') as software:
    reader =  csv.DictReader(software)
    for row in reader:
        print((" {} has {} users.").format(row["name"],row["users"]))


users = [{"name":"Rajeev Kumar","username":"rk@gmail.com","password":"Rk@1234","department":"IT"},{"name":"chamcham Kumari","username":"chmmoo@gmail.com","password":"Ck@1234","department":"Medical"}]

keys = ["name","username","department"]
with open('document.csv' , 'w') as software:
    writer = csv.DictWriter(software,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)