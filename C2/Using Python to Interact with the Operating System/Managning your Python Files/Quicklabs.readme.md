The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/\*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
student-00-cd140e1b7d68@linux-instance:~$ cd data
student-00-cd140e1b7d68@linux-instance:~/data$ ls
employees.csv
student-00-cd140e1b7d68@linux-instance:~/data$ cat employees.csv
Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure
student-00-cd140e1b7d68@linux-instance:~/data$ cd ~/scripts
student-00-cd140e1b7d68@linux-instance:~/scripts$ nano generate_report.py
student-00-cd140e1b7d68@linux-instance:~/scripts$ chmod +x generate_report.py
student-00-cd140e1b7d68@linux-instance:~/scripts$ ./generate_report.py
[{'Username': 'audrey', 'Department': 'Development', 'Full Name': 'Audrey Miller'} , {'Username': 'ardeng', 'Department': 'Sales', 'Full Name': 'Arden Garcia'}, {'Us ername': 'baileyt', 'Department': 'Human Resources', 'Full Name': 'Bailey Thomas'} , {'Username': 'sousa', 'Department': 'IT infrastructure', 'Full Name': 'Blake Sou sa'}, {'Username': 'nguyen', 'Department': 'Marketing', 'Full Name': 'Cameron Nguy en'}, {'Username': 'greyc', 'Department': 'Development', 'Full Name': 'Charlie Gre y'}, {'Username': 'chrisb', 'Department': 'User Experience Research', 'Full Name': 'Chris Black'}, {'Username': 'silva', 'Department': 'IT infrastructure', 'Full Na me': 'Courtney Silva'}, {'Username': 'darcy', 'Department': 'IT infrastructure', ' Full Name': 'Darcy Johnsonn'}, {'Username': 'elliotl', 'Department': 'Development' , 'Full Name': 'Elliot Lamb'}, {'Username': 'halls', 'Department': 'Sales', 'Full Name': 'Emery Halls'}, {'Username': 'flynn', 'Department': 'Marketing', 'Full Name ': 'Flynn McMillan'}, {'Username': 'harley', 'Department': 'Human Resources', 'Ful l Name': 'Harley Klose'}, {'Username': 'jeanm', 'Department': 'Vendor operations', 'Full Name': 'Jean May Coy'}, {'Username': 'kstev', 'Department': 'Sales', 'Full Name': 'Kay Stevens'}, {'Username': 'lion', 'Department': 'User Experience Researc h', 'Full Name': 'Lio Nelson'}, {'Username': 'tillas', 'Department': 'Vendor opera tions', 'Full Name': 'Logan Tillas'}, {'Username': 'micah', 'Department': 'Develop ment', 'Full Name': 'Micah Lopes'}, {'Username': 'solm', 'Department': 'IT infrast ructure', 'Full Name': 'Sol Mansi'}]
student-00-cd140e1b7d68@linux-instance:~/scripts$ nano generate_report.py
student-00-cd140e1b7d68@linux-instance:~/scripts$ ./generate_report.py
[{'Department': 'Development', 'Username': 'audrey', 'Full Name': 'Audrey Miller'} , {'Department': 'Sales', 'Username': 'ardeng', 'Full Name': 'Arden Garcia'}, {'De partment': 'Human Resources', 'Username': 'baileyt', 'Full Name': 'Bailey Thomas'} , {'Department': 'IT infrastructure', 'Username': 'sousa', 'Full Name': 'Blake Sou sa'}, {'Department': 'Marketing', 'Username': 'nguyen', 'Full Name': 'Cameron Nguy en'}, {'Department': 'Development', 'Username': 'greyc', 'Full Name': 'Charlie Gre y'}, {'Department': 'User Experience Research', 'Username': 'chrisb', 'Full Name': 'Chris Black'}, {'Department': 'IT infrastructure', 'Username': 'silva', 'Full Na me': 'Courtney Silva'}, {'Department': 'IT infrastructure', 'Username': 'darcy', ' Full Name': 'Darcy Johnsonn'}, {'Department': 'Development', 'Username': 'elliotl' , 'Full Name': 'Elliot Lamb'}, {'Department': 'Sales', 'Username': 'halls', 'Full Name': 'Emery Halls'}, {'Department': 'Marketing', 'Username': 'flynn', 'Full Name ': 'Flynn McMillan'}, {'Department': 'Human Resources', 'Username': 'harley', 'Ful l Name': 'Harley Klose'}, {'Department': 'Vendor operations', 'Username': 'jeanm', 'Full Name': 'Jean May Coy'}, {'Department': 'Sales', 'Username': 'kstev', 'Full Name': 'Kay Stevens'}, {'Department': 'User Experience Research', 'Username': 'lio n', 'Full Name': 'Lio Nelson'}, {'Department': 'Vendor operations', 'Username': 't illas', 'Full Name': 'Logan Tillas'}, {'Department': 'Development', 'Username': 'm icah', 'Full Name': 'Micah Lopes'}, {'Department': 'IT infrastructure', 'Username' : 'solm', 'Full Name': 'Sol Mansi'}]
{'User Experience Research': 2, 'Development': 4, 'Marketing': 2, 'Vendor operatio ns': 2, 'Human Resources': 2, 'IT infrastructure': 4, 'Sales': 3}
student-00-cd140e1b7d68@linux-instance:~/scripts$ nano generate_report.py
student-00-cd140e1b7d68@linux-instance:~/scripts$ ./generate_report.py
[{'Department': 'Development', 'Username': 'audrey', 'Full Name': 'Audrey Miller'} , {'Department': 'Sales', 'Username': 'ardeng', 'Full Name': 'Arden Garcia'}, {'De partment': 'Human Resources', 'Username': 'baileyt', 'Full Name': 'Bailey Thomas'} , {'Department': 'IT infrastructure', 'Username': 'sousa', 'Full Name': 'Blake Sou sa'}, {'Department': 'Marketing', 'Username': 'nguyen', 'Full Name': 'Cameron Nguy en'}, {'Department': 'Development', 'Username': 'greyc', 'Full Name': 'Charlie Gre y'}, {'Department': 'User Experience Research', 'Username': 'chrisb', 'Full Name': 'Chris Black'}, {'Department': 'IT infrastructure', 'Username': 'silva', 'Full Na me': 'Courtney Silva'}, {'Department': 'IT infrastructure', 'Username': 'darcy', ' Full Name': 'Darcy Johnsonn'}, {'Department': 'Development', 'Username': 'elliotl' , 'Full Name': 'Elliot Lamb'}, {'Department': 'Sales', 'Username': 'halls', 'Full Name': 'Emery Halls'}, {'Department': 'Marketing', 'Username': 'flynn', 'Full Name ': 'Flynn McMillan'}, {'Department': 'Human Resources', 'Username': 'harley', 'Ful l Name': 'Harley Klose'}, {'Department': 'Vendor operations', 'Username': 'jeanm', 'Full Name': 'Jean May Coy'}, {'Department': 'Sales', 'Username': 'kstev', 'Full Name': 'Kay Stevens'}, {'Department': 'User Experience Research', 'Username': 'lio n', 'Full Name': 'Lio Nelson'}, {'Department': 'Vendor operations', 'Username': 't illas', 'Full Name': 'Logan Tillas'}, {'Department': 'Development', 'Username': 'm icah', 'Full Name': 'Micah Lopes'}, {'Department': 'IT infrastructure', 'Username' : 'solm', 'Full Name': 'Sol Mansi'}]
student-00-cd140e1b7d68@linux-instance:~/scripts$ ./generate_report.py
[{'Department': 'Development', 'Username': 'audrey', 'Full Name': 'Audrey Miller'} , {'Department': 'Sales', 'Username': 'ardeng', 'Full Name': 'Arden Garcia'}, {'De partment': 'Human Resources', 'Username': 'baileyt', 'Full Name': 'Bailey Thomas'} , {'Department': 'IT infrastructure', 'Username': 'sousa', 'Full Name': 'Blake Sou sa'}, {'Department': 'Marketing', 'Username': 'nguyen', 'Full Name': 'Cameron Nguy en'}, {'Department': 'Development', 'Username': 'greyc', 'Full Name': 'Charlie Gre y'}, {'Department': 'User Experience Research', 'Username': 'chrisb', 'Full Name': 'Chris Black'}, {'Department': 'IT infrastructure', 'Username': 'silva', 'Full Na me': 'Courtney Silva'}, {'Department': 'IT infrastructure', 'Username': 'darcy', ' Full Name': 'Darcy Johnsonn'}, {'Department': 'Development', 'Username': 'elliotl' , 'Full Name': 'Elliot Lamb'}, {'Department': 'Sales', 'Username': 'halls', 'Full Name': 'Emery Halls'}, {'Department': 'Marketing', 'Username': 'flynn', 'Full Name ': 'Flynn McMillan'}, {'Department': 'Human Resources', 'Username': 'harley', 'Ful l Name': 'Harley Klose'}, {'Department': 'Vendor operations', 'Username': 'jeanm', 'Full Name': 'Jean May Coy'}, {'Department': 'Sales', 'Username': 'kstev', 'Full Name': 'Kay Stevens'}, {'Department': 'User Experience Research', 'Username': 'lio n', 'Full Name': 'Lio Nelson'}, {'Department': 'Vendor operations', 'Username': 't illas', 'Full Name': 'Logan Tillas'}, {'Department': 'Development', 'Username': 'm icah', 'Full Name': 'Micah Lopes'}, {'Department': 'IT infrastructure', 'Username' : 'solm', 'Full Name': 'Sol Mansi'}]
student-00-cd140e1b7d68@linux-instance:~/scripts$ cd ~/data
student-00-cd140e1b7d68@linux-instance:~/data$ ls
employees.csv report.txt
student-00-cd140e1b7d68@linux-instance:~/data$ cat report.txt
Development:4
Human Resources:2
IT infrastructure:4
Marketing:2
Sales:3
User Experience Research:2
Vendor operations:2
student-00-cd140e1b7d68@linux-instance:~/data$
